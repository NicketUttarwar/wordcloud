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

wordcloud = WordCloud().generate(data)
#and use matplotlib to display generated image
plt.imshow(wordcloud)
plt.axis("off")
# plt.show()


# plt.imshow(cloud_mask)
# plt.axis("off")
# plt.show()
fig1=plt.gcf()
# plt.show()
# plt.draw()
fig1.savefig("35-wordcl.svg", format="svg", bbox_inches="tight")
