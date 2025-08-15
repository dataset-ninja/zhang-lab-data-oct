Dataset **ZhangLabData: OCT** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMzIyOF9aaGFuZ0xhYkRhdGE6IE9DVC96aGFuZ2xhYmRhdGEtb2N0LURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIms1VWZKOFBPSk9EQmZ2N2xtNThkQklkREk2czcyTmhHd1hHMFJIR3JMRXM9In0=?response-content-disposition=attachment%3B%20filename%3D%22zhanglabdata-oct-DatasetNinja.tar%22)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='ZhangLabData: OCT', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/rscbjbr9sj-3.zip).