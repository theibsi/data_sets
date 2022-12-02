import pydicom
import os


def file_generator(main_dir):

    patient_names = os.listdir(main_dir)

    for patient_name in patient_names:
        for modality in ["CT", "PET", "MR_T1"]:
            img_dir = os.path.join(main_dir, patient_name, modality, "image")
            img_file = os.listdir(img_dir)[0]
            img_file = os.path.join(img_dir, img_file)

            roi_dir = os.path.join(main_dir, patient_name, modality, "mask")
            roi_file = os.listdir(roi_dir)[0]
            roi_file = os.path.join(roi_dir, roi_file)

            yield img_file, roi_file


for image_file, roi_file in file_generator(main_dir=r"C:\Users\alexz\Documents\GitHub\data_sets\ibsi_validation\dicom"):
    img_dcm = pydicom.dcmread(image_file)
    roi_dcm = pydicom.dcmread(roi_file)

    img_dcm_series_uid = img_dcm["SeriesInstanceUID"]
    img_dcm_series_frame_of_reference_uid = img_dcm["FrameOfReferenceUID"]

    roi_updated = False

    for for_dcm_seq in roi_dcm["ReferencedFrameOfReferenceSequence"]:
        if str(for_dcm_seq["FrameOfReferenceUID"].value) != str(img_dcm_series_frame_of_reference_uid.value):
            for_dcm_seq.FrameOfReferenceUID = str(img_dcm_series_frame_of_reference_uid.value)
            roi_updated = True

        for ref_study_dcm_seq in for_dcm_seq["RTReferencedStudySequence"]:
            for ref_series_dcm_seq in ref_study_dcm_seq["RTReferencedSeriesSequence"]:
                if str(ref_series_dcm_seq["SeriesInstanceUID"].value) != str(img_dcm_series_uid.value):
                    ref_series_dcm_seq.SeriesInstanceUID = str(img_dcm_series_uid.value)
                    roi_updated = True

    if roi_updated:
        roi_dcm.save_as(roi_file)
