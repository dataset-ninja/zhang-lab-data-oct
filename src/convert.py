import os
import shutil
from urllib.parse import unquote, urlparse

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
    list_files_recursively,
)
from tqdm import tqdm

import src.settings as s


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "bone classification and detection"
    dataset_path = "/home/grokhi/rawdata/large-oct-chest-dataset/CellData/chest_xray"

    images_ext = ".jpeg"
    # ann_ext = ".txt"
    batch_size = 30

    ds_name_to_data = {
        "train": "/home/grokhi/rawdata/large-oct-chest-dataset/CellData/OCT/train",
        "test": "/home/grokhi/rawdata/large-oct-chest-dataset/CellData/OCT/test",
    }

    def create_ann(image_path):
        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        tag_name = image_path.split("/")[-2]
        tags = [sly.Tag(tag_meta) for tag_meta in tag_metas if tag_name in tag_meta.name]

        return sly.Annotation(img_size=(img_height, img_wight), img_tags=tags)

    tag_names = ["NORMAL", "CNV", "DME", "DRUSEN"]
    tag_metas = [sly.TagMeta(name, sly.TagValueType.NONE) for name in tag_names]

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(tag_metas=tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    for ds_name, data_path in ds_name_to_data.items():
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        images_paths = list_files_recursively(data_path, [images_ext])
        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_paths))

        for images_paths_batch in sly.batched(images_paths, batch_size=batch_size):
            images_names_batch = [
                get_file_name_with_ext(image_path) for image_path in images_paths_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, images_names_batch, images_paths_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in images_paths_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(images_names_batch))

    return project
