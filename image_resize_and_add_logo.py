'''
    About us:
    
        Youtube Channel:  bit.ly/shencshegidzlia
        Facebook Page  :  fb.me/shencshegidzlia
        Email:            info.shencshegidzlia@gmail.com

        შენც შეგიძლია!
        05.06.2018
        
'''


def help_():
    result = r'''

            ფუნქცია საშუალებას გვაძლევს მოვახდინოთ სხვადასხვა ზომისა და ფორმატის სურათების
	სტანდარტულ ზომასა და ფორმატში გადაყვანა + სასურველი ზომის ლოგოს დადება ჩვენთვის სასურველ პოზიციაზე.
	საჭიროების შემთხვევაში გამოიყენება შავი ფერის ფონი სურათის შესავსებად.

            შესაძლებელია ნებისმიერი სიგრძისა და სიგანის კომბინაციის შერჩევა საბოლოო სურათებისთვის,
	ფუნქცია ცდილობს ამ სივრცის მაქსიმალურად გამოყენებას.

            ფუნქცია მუშაობს ბევრი სხვა გაფართოების სურათებისთვისაც,
	თუმცა ლოგოსა და სურათის სასურველი ფორმატებია jpg/jpeg და png.

არგუმენტები:
   1. imagesFolder - საქაღალდე, რომელშიც გვაქვს საწყისი სურათები

   2. resultsFolder - საქაღალდე, რომელშიც გვსურს შედეგების შენახვა(სურათების სახელები დარჩება უცვლელი) 

   3. final_image_dimensions - საწყისი სურათისგან მისაღები სასურველი სურათის განზომილებები - 
   							   სიგანე(width) და სიგრძე(height) პიქსელებში.

	   თუ არგუმენტად გამოვიყენებთ მხოლოდ ერთ რიცხვს(integer), (მაგ: 1500)
	       მიღებული სურათის სიგრძე და სიგანე 1500 პიქსელის ტოლი იქნება.

	   შესაძლებელია განსხვავებული სიგრძისა და სიგანის კომბინაციების გამოყენებაც სიის სახით,
	       მაგ: (1500, 1000) - ამ შემთხვევაში, საბოლოო სურათის სიგანე იქნება 1500,
   							                                 სიგრძე - 1000 პიქსელი.
   							                                 
   4. newExtension - შედეგად მიღებული სურათის სასურველი გაფართოება (მაგ: jpg/jpeg, png ...).
					 მაგ: შესაძლებელია საწყისი სურათის გაფართოება იყოს jpg და საბოლოო სურათის png.

   5. file_position_percentage_logoCompareDimension_distances:

       თუ არ გვსურს სურათზე ლოგოს დამატება, ამ არგუმენტში შეგვიძლია მივუთითოთ ნებისმიერი Falsy მნიშვნელობა, ანუ
       მონაცემი, რომელიც შეფასდება როგორც False/მცდარი.
       მაგალითად: [] ან {} ან () ან "" ან 0 ან 0.0 ან None ან False

       თუ გვსურს ლოგოს დამატებაც, არგუმენტში ვუთითებთ 5 მონაცემისგან შემდგარ სიას, შემდეგი თანმიმდევრობით:
           1. file - ლოგოს ფაილის მისამართი (მაგ: r"C:\Users\user\Desktop\logo.png")

           2. position - რიცხვი 1-დან 4-მდე, 
              შესაბამისად ლოგოს მოთავსებისთვის გაითვალისწინება განსხვავებული კუთხეები:
                           					1 - ზედა მარცხენა 
                           					2 - ზედა მარჯვენა
                           					3 - ქვედა მარცხენა
                           					4 - ქვედა მარჯვენა

           3. percentage - საბოლოო სურათის სიგრძის/სიგანის რა ნაწილი გვინდა დაიკავოს ლოგომ(პროცენტებში)

           4. logoCompareDimension - წინა არგუმენტში მითითებული პროცენტის გამოთვლა
           							 საბოლოო სურათის სიგანისთვის მოხდეს თუ სიგრძისთვის, შესაბამისად
           							  		   "W" - სიგანისთვის(width) 
           							 					ან
           							 		   "H" - სიგრძისთვის(height)
			 მაგ:
			    თუ percentage-ში მივუთითებთ 100-ს და ამ არგუმენტში "W"-ს,
			    ჩასასმელი ლოგოს ზომა(მიუხედავად საწყისი ლოგოს ზომისა)
			    გახდება იმხელა, რომ სრულად დაიკავოს საბოლოო სურათის სიგანე.

           5. distances - შერჩეული კუთხიდან რა მანძილიდან დაიწყოს ლოგოს ჩასმა, გვჭირდება 2 რიცხვისგან შემდგარი სია 
           								    (ჰორიზონტალური და ვერტიკალური დაშორება)

			  მაგ_1: (0, 100) - შემთხვევაში, თუ position=1-ს, ანუ ვიყენებთ ზედა მარცხენა კუთხეს,
			  	  ლოგოს ჩასმა დაიწყება ზედა მარცხენა კუთხიდან 0 პიქსელით მარჯვნივ და 100 პიქსელით ქვემოთ მდებარე პიქსელიდან.
			  	  ლოგო განთავსდება ამ პიქსელის ქვემოთ და მარჯვნივ.

			  მაგ_2: (10, 40) - შემთხვევაში, თუ position=4-ს, ანუ ვიყენებთ ქვედა მარჯვენა კუთხეს,
			  	  ლოგოს ჩასმა დაიწყება ქვედა მარჯვენა კუთხიდან 10 პიქსელით მარცხნივ და 40 პიქსელით ზემოთ მდებარე პიქსელიდან.
			  	  ლოგო განთავსდება ამ პიქსელის ზემოთ და მარცხნივ.

'''

    return result


def logo_and_resize(imagesFolder,resultsFolder, final_image_dimensions, newExtension, file_position_percentage_logoCompareDimension_distances):
    # import
    import os, time
    from PIL import Image
                    
    # get images list from folder
    enumerated_images_list = list(enumerate(os.listdir(imagesFolder))) # get list of images
    # welcome
    print("\n", "| Process Started, number of images |{}|. |".center(70, "=").format(len(enumerated_images_list)), "\n", sep="")
    
    ''' work with final image dimensions '''
    if isinstance(final_image_dimensions, int):  # if only one argument is given as integer, image will be square
        final_image_width = final_image_height = final_image_dimensions
    elif len(final_image_dimensions) == 2:
        final_image_width, final_image_height = final_image_dimensions
    else:
        print("\n", "| Something is wrong with final image dimensions. |".center(70, "-"))
        return # stop process
    # get max dimension
    final_image_max_dimension = max(final_image_width,final_image_height)
    
    ''' do we want logo to be added ? '''
    if file_position_percentage_logoCompareDimension_distances: # we should use anu type of Falsy value("", [], ()...) for this argument if we do not want logo to be added
        # assign them to corresponding variables        
        logoFile, logo_position, logoSizePercentage,logoCompareDimension, logo_distance_from_corners = file_position_percentage_logoCompareDimension_distances
        # try to open logo file
        try: 
            logo = Image.open(logoFile)
        except Exception as e:
            print("We can not load logo file. | " + str(e))
            return # stop process
    else:
          print("| Logo will not be added. |".center(70, "-"), "\n")

    ''' do main part '''
    for index, imageName in enumerated_images_list:  # for each image in folder
        # create background
        background = Image.new("RGB",(final_image_width, final_image_height), color = (0,0,0))  # color=(255,255,255) ==> to get white background
        try:
            # for each image
            image = Image.open(os.path.join(imagesFolder,imageName))  #Open Image
            width, height = image.size  #Get dimensions
            ratio = width / height   #get ratio
            newHeight,newWidth  = height, width #Define new height and width
            # get old image name + new(maybe same) extension
            old_image_name = "".join(imageName.split(".")[:-1])
            # and define new image name
            new_image_name_with_extension = old_image_name + "." +  newExtension

            ''' not square cases image resize'''
            # adjust by height
            if height / final_image_height != 1:
                coefficient = height / final_image_height

                newHeight = height / coefficient
                newWidth = width / coefficient
            # adjust by width, if necessary
            if newWidth > final_image_width:
                coefficient = newWidth / final_image_width

                newWidth = newWidth / coefficient
                newHeight = newHeight / coefficient
                
            ''' Center images on background '''
            startSide = int((final_image_width - newWidth)/2) 
            startUp = int((final_image_height - newHeight)/2) 
            pastePositions = (startSide, startUp)
            
            # new Dimensions
            resizedDimensions = (int(round(newWidth,0)),int(round(newHeight,0) ))  #round and convert to integers
            # get resized image
            resized = image.resize(resizedDimensions)
            # paste image on background
            background.paste(resized,(pastePositions))
            
            ''' work with logo '''
            if file_position_percentage_logoCompareDimension_distances:
                ''' logo dimensions '''
                try: 
                    logoStartWidth, logoStartHeight = logo.size
                    logo_ratio = logoStartWidth / logoStartHeight  # width / height
                    # calculate dimensions of logo
                    if logoCompareDimension.upper() ==  "W":  # this argument should be W for width or H for height, casing does not matter
                        logo_width = int(round((final_image_width * logoSizePercentage) / 100))
                        logo_height = int(round(logo_width / logo_ratio))
                    elif logoCompareDimension.upper() == "H":
                        logo_height = int(round((final_image_height * logoSizePercentage) / 100))
                        logo_width = int(round(logo_height * logo_ratio))
                    else:
                        print("\n", "| Please use H for height or W for width as logo percentage check dimension. |".center(90, "-"))
                        return # stop process
                    
                    logo_to_add = logo.resize((logo_width, logo_height))

                    ''' work with logo placement '''
                    # how far away should logo be added from its corner (x, y)
                    x_distance, y_distance = logo_distance_from_corners
                    # work with different corners, set starting x and y coordinates for logo starting point
                    if logo_position == 1:
                        x_start = x_distance
                        y_start = y_distance
                    elif logo_position == 2:
                        x_start = final_image_width - (x_distance + logo_width)
                        y_start = y_distance
                    elif logo_position == 3:
                        x_start = x_distance
                        y_start = final_image_height - (y_distance + logo_height)
                    elif logo_position == 4:
                        x_start = final_image_width - (x_distance + logo_width)
                        y_start = final_image_height - (y_distance + logo_height)
                    else:
                        print("| Please use logo position argument from 1 to 4.| ".center(70))
                        return # stop process

                    # use defined x and y
                    logo_add_start = (x_start, y_start)
                    ''' paste logo '''
                    try:
                        background.paste(logo_to_add,logo_add_start,logo_to_add) # also works for png logos
                    except:
                        background.paste(logo_to_add,logo_add_start) # for not png
                    
                except Exception as e:
                    print("\n", "| Something went wrong with logo. |".center(70, "-"), "\n")
            #Save
            background.save(os.path.join(resultsFolder,new_image_name_with_extension))
            print(str(index + 1).ljust(2) + "| " + new_image_name_with_extension.ljust(40) + "| + |")

        except Exception as e:
            print(e)
            
    # completed
    print("\n", "| Completed |".center(70, "*"), "\n")
