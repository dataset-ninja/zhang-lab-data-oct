The **Large Dataset of Labeled Optical Coherence Tomography (OCT) and Chest X-Ray Images** encountered challenges related to reliability and interpretability in implementing clinical-decision support algorithms for medical imaging. They embarked on developing a diagnostic tool utilizing a deep-learning framework specifically designed for screening patients with common treatable blinding retinal diseases. The final OCT dataset contains 108,312 images.

## Spectral-Domain OCT Imaging

The primary application was in the diagnosis of retinal OCT images. Spectral-domain OCT captures high-resolution optical cross sections of the retina, assembling them into three-dimensional-volume images. It has become a widely performed medical imaging procedure, particularly in diagnosing age-related macular degeneration (AMD) and diabetic macular edema.

OCT imaging has become a standard of care in guiding the diagnosis and treatment of leading causes of blindness, including AMD and diabetic macular edema. The prevalence of these diseases is significant, with millions affected, and the utilization of anti-vascular endothelial growth factor (anti-VEGF) medications has revolutionized treatment.

## Dataset Details and Training Outcome

The authors obtained 207,130 OCT images initially, with 108,312 images passing quality review for training the AI system. Testing involved 1,000 images from 633 patients. After 100 epochs, training was halted due to the absence of further improvement in both accuracy and cross-entropy loss.

An independent test set of 1,000 images was used to compare the AI network's referral decisions with those of human experts. The AI system's performance was comparable to human experts in distinguishing patients needing urgent referral.

The authors conducted an occlusion test on 491 images to identify areas contributing most to the neural network's assignment of the predicted diagnosis. The testing successfully identified regions of interest, demonstrating high accuracy in recognizing clinically significant areas of pathology.


