IBSI-1 MR validation dataset
===

This dataset was used to validate the findings in the IBSI 1 study. The `Glnd_Submand_L` contour was used.

The phantom is available in both DICOM and NIfTI formats, and consists of the image itself (image) and its segmentation (mask).
The segmentation in DICOM format is an RTSTRUCT and needs to be converted to a voxel mask, whereas in the NIfTI format, the mask is already a voxel mask.
Consider using the NIfTI mask in case conversion of in-plane polygons to a mask is not supported.

## License
The phantom is licensed under the Creative Commons Attribution 3.0 Unported Licence. To view a copy of this license, visit https://creativecommons.org/licenses/by/3.0/ or send a letter to Creative Commons, PO Box 1866, Mount View, CA 94042, USA.

## Acknowledgments
This dataset is based on the T2-weighted MRI image and contours of the RTMAC_TRAIN_001 set that was used in the AAPM RT-MAC Grand Challenge 2019, and uploaded to the Cancer Imaging Archive. The derived dataset is calibrated so that all intensities fall in the $[0, \infty)$ range, with 1.0 corresponding the 98th percentile of the intensities in the image. The procedure is similar to standardisation using z-normalisation, but does not assume normal distribution of the intensities.

Alex Zwanenburg:
* used the Otsu thresholding algorithm with subsequent morphological closing (sphere of 5mm radius) to define a patient mask.
* derived the 2nd and 98th percentile ($p_2$, $p_{98}$) values of voxels in the mask.
* normalised voxel intensities through a linear transformation so that voxels with intensities in the range $[p_2, p_{98}]$ are linearly mapped to $[0.0, 1.0]$.
* saturated intensities below 0.0, so that all intensities are mapped to $[0, \infty)$.
* isolated the `Glnd_Submand_L` contour.
* cropped the image 5 cm around the contour.
* exported the image and contour to DICOM format.
* converted the image and the mask from DICOM and RTSTRUCT formats to NIfTI format.

The above operations were performed using MIRP (https://github.com/oncoray/mirp).

## Citation information
Please include the following citations when using this dataset:

* Cardenas, C., Mohamed, A., Sharp, G., Gooding, M., Veeraraghavan, H., Yang, J. (2019). Data from AAPM RT-MAC Grand Challenge 2019. The Cancer Imaging Archive. DOI: 10.7937/tcia.2019.bcfjqfqb
* Clark, K., Vendt, B., Smith, K., Freymann, J., Kirby, J., Koppel, P., Moore, S., Phillips, S., Maffitt, D., Pringle, M., Tarbox, L., Prior, F. The Cancer Imaging Archive (TCIA): Maintaining and Operating a Public Information Repository, Journal of Digital Imaging, Volume 26, Number 6, December, 2013, pp 1045-1057. DOI: 10.1007/s10278-013-9622-7