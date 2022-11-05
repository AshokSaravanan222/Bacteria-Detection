# Medical-Interventions-SkinCancerPaper
For my Medical Interventions PLTW class, I was asked to appoximate the percentage of bacteria that grew on the image of a petri dish. Although this seems like a simple, and straightforward task, I had to get machine learning involved.

In order to do so, I used cv2 and image processing to detect the percentage of bacteria in the 4 follwing four images: MTB, MTF, WTB, WTF. I am describing how I used machine learning here, but if you want to understand the context here is the link to the full paper: https://docs.google.com/document/d/1USXceapfN2R6_XSefxFygamXU7Pn9Z_BCcb1Bj7iocM/edit?usp=sharing

Here are some pictures of the differnt steps of the program:

**Step 1: Find petri dish circle outline/center split**

![normal](https://user-images.githubusercontent.com/90977640/200098218-ce330da8-ff85-4fb5-9c58-c8ab2e38f041.jpg)

**Step 2: Convert images to grayscale and split according to outline**

![grayscale](https://user-images.githubusercontent.com/90977640/200098226-b69eea5e-5770-46cc-8e46-1d18a76d6f2a.jpg)


**Step 3: Detect area percentage based on amount of darker pixels**

![image3](https://user-images.githubusercontent.com/90977640/200098233-790eaefe-9fa3-4010-acfb-521793f69793.jpg)

# Conclusion/Results

I think there were some problems with the implementation of my code, since the results were a little varied when comapred to the control: I think this is because of the lighting. However, I think this is still much better than just approximating.
