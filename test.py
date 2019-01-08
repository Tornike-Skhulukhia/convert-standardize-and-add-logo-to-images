from image_resize_and_add_logo import help_ , logo_and_resize

##print(help_())




''' logo_and_resize( imagesFolder,
                     resultsFolder,
                     final_image_dimensions,
                     newExtension,
                     file_position_percentage_logoCompareDimension_distances) '''
# file_position_percentage_logoCompareDimension_distances
logo_args = (r"C:\Users\user\Desktop\Add_logos_on_images_4.6.2018\logo\google.png",
             4,
             30,
             "W",
             (50,50))



logo_and_resize(r"C:\Users\user\Desktop\Add_logos_on_images_4.6.2018\images",
                r"C:\Users\user\Desktop\Add_logos_on_images_4.6.2018\converted",
                (3000, 1800),
                "jpg",
                logo_args)
                
                
                
