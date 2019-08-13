IBSI-1 FDG-PET validation dataset
===

This data set was used to validate the findings in the IBSI 1 study. The `GTV` contour was used.

The phantom is available in both DICOM and NIfTI formats, and consists of the image itself (image) and its segmentation (mask).
The segmentation in DICOM format is an RTSTRUCT and needs to be converted to a voxel mask, whereas in the NIfTI format, the mask is already a voxel mask.
Consider using the NIfTI mask in case conversion of in-plane polygons to a mask is not supported.

## License
The phantom is licensed under the Creative Commons Attribution 3.0 Unported Licence. To view a copy of this license, visit https://creativecommons.org/licenses/by/3.0/ or send a letter to Creative Commons, PO Box 1866, Mount View, CA 94042, USA.

## Acknowledgments
This dataset is based on the CT image and contours of the HN-HGJ-001 set of the Head-Neck-PET-CT collection that was uploaded to the Cancer Imaging Archive.

Alex Zwanenburg:

* converted uptake activity to SUV using body-weight normalisation.
* isolated the `GTV` contour.
* cropped the image 5 cm around the contour.
* exported the image and contour to DICOM format.
* converted the image and the mask from DICOM and RTSTRUCT formats to NIfTI format.

The above operations were performed using MIRP (https://github.com/oncoray/mirp).

## Citation information
Please include the following citations when using this dataset:

* Vallières, M., Kay-Rivest, E., Perrin, L. J., Liem, X., Furstoss, C., Khaouam, N., Nguyen-Tan, P. F., Wang, C.-S., Sultanem, K. (2017). Data from Head-Neck-PET-CT. The Cancer Imaging Archive. DOI: 10.7937/K9/TCIA.2017.8oje5q00
* Vallières, M. et al. Radiomics strategies for risk assessment of tumour failure in head-and-neck cancer. Sci Rep 7, 10117 (2017). DOI: 10.1038/s41598-017-10371-5
* Clark, K., Vendt, B., Smith, K., Freymann, J., Kirby, J., Koppel, P., Moore, S., Phillips, S., Maffitt, D., Pringle, M., Tarbox, L., Prior, F. The Cancer Imaging Archive (TCIA): Maintaining and Operating a Public Information Repository, Journal of Digital Imaging, Volume 26, Number 6, December, 2013, pp 1045-1057. DOI: 10.1007/s10278-013-9622-7