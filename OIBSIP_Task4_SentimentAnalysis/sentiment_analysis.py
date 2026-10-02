import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report, confusion_matrix
from wordcloud import WordCloud

df=pd.read_csv("sentiment_reviews.csv")
print("Class distribution:\n",df["Sentiment"].value_counts())
try:
    from nltk.corpus import stopwords
    STOP_WORDS=set(stopwords.words("english"))
except Exception:
    STOP_WORDS={"the","is","a","an","and","or","to","of","in","on","for","with","this","that","it","i","my","was","are"}

def preprocess(text):
    text=re.sub(r"[^a-z\\s]"," ",str(text).lower())
    return " ".join(w for w in text.split() if w not in STOP_WORDS)

df=df.dropna(subset=["Review","Sentiment"]).drop_duplicates("Review").copy()
df["Clean_Review"]=df["Review"].apply(preprocess)
X_train_text,X_test_text,y_train,y_test=train_test_split(df["Clean_Review"],df["Sentiment"],test_size=.20,random_state=42,stratify=df["Sentiment"])
vec=TfidfVectorizer(ngram_range=(1,2)); X_train=vec.fit_transform(X_train_text); X_test=vec.transform(X_test_text)
models={"Naive Bayes":MultinomialNB(),"Logistic Regression":LogisticRegression(max_iter=1000)}
results=[]
predictions={}
for name,m in models.items():
    m.fit(X_train,y_train); pred=m.predict(X_test); predictions[name]=pred
    p,r,f1,_=precision_recall_fscore_support(y_test,pred,average="weighted",zero_division=0)
    results.append([name,accuracy_score(y_test,pred),p,r,f1])
    print("\n",name,"\n",classification_report(y_test,pred,zero_division=0))
print(pd.DataFrame(results,columns=["Model","Accuracy","Precision","Recall","F1-score"]).round(4))
for name,pred in predictions.items():
    cm=confusion_matrix(y_test,pred,labels=["negative","neutral","positive"])
    sns.heatmap(cm,annot=True,fmt="d",cmap="Blues",xticklabels=["negative","neutral","positive"],yticklabels=["negative","neutral","positive"])
    plt.title(name+" - Confusion Matrix"); plt.xlabel("Predicted"); plt.ylabel("Actual"); plt.show()
sns.countplot(data=df,x="Sentiment",order=["negative","neutral","positive"]); plt.title("Sentiment Distribution"); plt.show()
for s in ["negative","neutral","positive"]:
    text=" ".join(df.loc[df.Sentiment==s,"Clean_Review"])
    plt.figure(figsize=(10,5)); plt.imshow(WordCloud(width=900,height=450,background_color="white").generate(text)); plt.axis("off"); plt.title("WordCloud - "+s.title()); plt.show()
pred=predictions["Logistic Regression"]
errors=pd.DataFrame({"Review":df.loc[X_test_text.index,"Review"],"Actual":y_test,"Predicted":pred})
print("\nFive misclassified examples:\n",errors[errors.Actual!=errors.Predicted].head(5).to_string(index=False))
