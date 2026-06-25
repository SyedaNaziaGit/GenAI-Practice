from langchain_core.runnables import  RunnableLambda
#normal function can be converted into runnable user the RunnableLambda builtin
def word_counter(text):
    return len(text.split())

#converting the above python function or any lambda function into a runnable
runnable_word_counter = RunnableLambda(word_counter)
print(runnable_word_counter.invoke("Hi how u?"))