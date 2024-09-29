
import streamlit as st
from PIL import Image, ImageDraw, ImageGrab
import numpy as np
from io import StringIO



# def model(picture) -> list:
#     # initialize the client
#     CLIENT = InferenceHTTPClient(
#         api_url="https://detect.roboflow.com",
#         api_key="U56nnxvhT8UmyFW19P8U"
#     )

#     # infer on a local image
#     result = CLIENT.infer(picture, model_id="mhacks/1")

#     return result;


# def processing(picture) -> int:

#     image = cv2.imread(picture, cv2.IMREAD_GRAYSCALE)

#     x, y, w, h = 100, 100, 100, 100
#     threshold_value = 200
#     max_value = 255

#     # _, binary_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

#     st.image(binary(image))
#     contour_images, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


#     for contour in contour_images:
#         perimeter = cv2.arcLength(contour, True)

#         st.write(perimeter)
#         dims = cv2.approxPolyDP(contour, 0.02 * perimeter, True)



#         # st.write(type(dims[0]))
#         if len(dims) == 4:
#             x, y, w, h = cv2.boundingRect(dims)
#             st.write([x, y, w, h])
            
#             # cv2.drawContours(picture, [dims], -1, (0, 255, 0), 3)
#             # cv2.putText(
#             #     image,
#             #     "rectange", 
#             #     (x, y-10),
#             #     (cv2.FONT_HERSHEY_SIMPLEX), 
#             #     0.5,
#             #     (0, 255, 0),
#             #     2,
#             # )

#     # st.image(contour_image)

#     # st.image(image)
#     return x, y, w, h

# def binary(image):
#     threshold_value, max_value = 150, 255;
#     _, binary_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)
#     return binary_image
    

def take_image():
      
    img_file_buffer = st.camera_input("Take a photo")

    if img_file_buffer is not None:

        img = Image.open(img_file_buffer)

        st.image(img)

        picture = "im.jpg"

        img.save(picture)

def file_upload():

    img_saved = st.file_uploader('upload a file')
    if img_saved is not None:

        bytes_data = img_saved.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(img_saved.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)


def main():
        file_upload()

        # res = model(picture)
        
        # print(res)

        # predictions = res['predictions'][0]

        # Iterate over the detected objects and draw the bounding boxes
        # x = int(predictions['x'])
        # y = int(predictions['y'])
        # w = int(predictions['width'])
        # h = int(predictions['height'])
        # x, y, w, h = processing(picture)

        # st.write([x,y,w,h])

        # draw = ImageDraw.Draw(img)

        # draw.rectangle((x, y, x + w, y + h), outline = 'red', width = 2)

        # img = img.convert('RBGA')

        # rectangles = [
        #     ((10, 10), (50, 50)),  # rectangle 1
        #     ((100, 100), (150, 150)),  # rectangle 2
        #     ((200, 200), (250, 250))  # rectangle 3
        # ]
       

        # draw = ImageDraw.Draw(img)

        # for rect in rectangles:
        #     x1, y1 = rect[0]
        #     w, h = rect[1]
        #     draw.rectangle((x1, y1, x1+w, y1+h), outline='red', width=2)

        # print(type(img))


        img_array = np.array(img)



        st.write(type(img_array))
        st.write(img_array.shape)



if __name__ == "__main__":
    main()