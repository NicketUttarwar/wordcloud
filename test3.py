from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 2000
import pandas as pd
import numpy as np
from PIL import Image

data = "Inclusivity Honesty Growth Collaboration Integrity Optimism Curiosity Community"

# wordcloud = WordCloud().generate(data)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()
print("starting cloud mask")
cloud_mask = np.array(Image.open("35-1.png"))
# plt.imshow(cloud_mask)
# plt.axis("off")
# plt.show()
print("finished cloud mask, starting wordcloud")

wordcloud = WordCloud(#font_path="Sitka.ttc", #add your font here
                      width = 571, # use the same width and height
                                    #as your mask size for best
                                    #results
                      height = 571,
                      #stopwords=STOPWORDS, #if the staple stopwords
                                           #the module provides is
                                           #not good enough, you can
                                           #list your own
                      background_color = "black",
                      mask = cloud_mask,
                      contour_width = 0,
                      repeat=True,
                      min_font_size = 2, #if you want a tight fit,
                                         #go for a small figure here
                      max_words = 1000, #set max words count
                      ).generate(data)
print("finished word cloud")

image_colors = ImageColorGenerator(cloud_mask) #use the mask colours
print("finished image colors")

wordcloud.generate(data)
wordcloud.recolor(color_func=image_colors)
plt.imshow(wordcloud)
plt.axis("off")
fig1=plt.gcf()
# plt.show()
plt.draw()
fig1.savefig("35-1-words-black.png", format="png", bbox_inches="tight")
