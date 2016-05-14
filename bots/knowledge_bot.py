import scraping_utils as scrap

def answer(question, confidence = 0.5):

    '''
    Answers a fact based question by scraping google.

    Parameters:
    ----------
    :param question: str
    :param confidence: float, default 0.5
        Required confidence level of the answer scraped. If answer is available right away on google,
        confidence level is 1.
    '''

    question = question.split(" ")
    question = '+'.join(question)

    url = 'https://www.google.com/search?q=' + question
    page = scrap.get_tree(url)

    answer = ''
    for t in page.findAll('div', {'class': '_XWk'}):
        answer = t.text

    if answer == '':
        print "Sorry. I really tried hard to get the information you were looking for. But, it seems like" \
              "I am not the right bot to answer your question! \n \n TIP: Be more specific!"

    else:
        print 'Answer: ', answer

    return answer

# Debug: Run only if this page is directly executed.
if __name__ == "__main__":
    question = raw_input("Ask a question! \n")
    answer(question)