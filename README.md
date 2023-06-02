# Server-project
This repository contains a Python API for uploading, optimizing, and serving images. The API leverages a message queue for efficient processing and load handling. Images are resized to different quality levels and can be fetched using unique IDs.

**Features**
**Image Upload Endpoint:** This API provides an endpoint to upload images. After receiving the image, it is pushed to a queue for further processing.

**Image Optimization:** Images from the queue are taken one by one for optimization. For each image, three smaller size variants are generated at 75%, 50%, and 25% quality levels.

**Image Serving Endpoint:** The API exposes an endpoint for downloading an image by its unique ID. You can specify the desired quality level of the image using query parameters.

