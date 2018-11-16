from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = """
Babson College is a private business school in Wellesley, Massachusetts, established in 1919. Its central focus is on entrepreneurship education, and it is often ranked the most prestigious entrepreneurship college in the United States.[3][4][5][6]

It was founded by Roger W. Babson as an all-male business institute. Now co-ed, Babson College offers bachelor's degrees in business administration and undergraduate students have the opportunity to declare concentrations in more than twenty seven areas of study. Through Babson's F. W. Olin Graduate School of Business, the college also offers master's degrees in business administration, finance, accounting, entrepreneurial leadership and management. Often referred to as the "Entrepreneur's College", Babson is renowned for immersing its students in the entrepreneurial lifestyle and culture. Babson is also notable for its Foundations of Management and Entrepreneurship course, in which every enrolled first-year student starts, runs and dissolves a company. Babson currently offers undergraduates nearly sixty entrepreneurship-related courses. These courses are taught in tandem with various traditional liberal arts courses, which represent over 60% of the typical student's schedule. Every entrepreneurship course at Babson is taught by professors who have either started, sold, bought, or run successful businesses.[7] Babson is considered very selective and currently has an undergraduate acceptance rate of 24%.[8]

Babson College has consistently appeared on the U.S. News & World Report rankings as the number one college in entrepreneurship education for nearly three decades. In 2014, CNN's Money Magazine named Babson the number one college in the country for value and in 2015 the magazine ranked it second.[9] The Economist ranked Babson second on its 2015 list of best colleges and universities in outperforming earnings expectations.[10] Babson's MBA program has also been ranked number one in entrepreneurship for over twenty years by U.S. News & World Report.
"""
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

sentence1 = """
Boston University (commonly referred to as BU) is a private, non-profit, research university in Boston, Massachusetts. The university is nonsectarian,[7] but has been historically affiliated with the United Methodist Church.[8][9]

The university has more than 3,900 faculty members and nearly 33,000 students, and is one of Boston's largest employers.[10] It offers bachelor's degrees, master's degrees, and doctorates, and medical, dental, business, and law degrees through 17 schools and colleges on two urban campuses. The main campus is situated along the Charles River in Boston's Fenway-Kenmore and Allston neighborhoods, while the Boston University Medical Campus is in Boston's South End neighborhood.

BU is categorized as an R1: Doctoral University (very high research activity) in the Carnegie Classification of Institutions of Higher Education.[11] BU is a member of the Boston Consortium for Higher Education[12] and the Association of American Universities. The University was ranked 37th among undergraduate programs at national universities, and 39th among global universities by U.S. News & World Report in its 2017 rankings.[13]

Among its alumni and current or past faculty, the university counts eight Nobel Laureates, 23 Pulitzer Prize winners, 10 Rhodes Scholars,[14][15] six Marshall Scholars,[16] 48 Sloan Fellows,[17] nine Academy Award winners, and several Emmy and Tony Award winners. BU also has MacArthur, Fulbright, Truman and Guggenheim Fellowship holders as well as American Academy of Arts and Sciences and National Academy of Sciences members among its past and present graduates and faculty. In 1876, BU professor Alexander Graham Bell invented the telephone in a BU lab.

The Boston University Terriers compete in the NCAA Division I. BU athletic teams compete in the Patriot League, and Hockey East conferences, and their mascot is Rhett the Boston Terrier. Boston University is well known for men's hockey, in which it has won five national championships, most recently in 2009.
"""
score1 = SentimentIntensityAnalyzer().polarity_scores(sentence1)
print(score1)

sentence2= """
Boston College (also referred to as BC) is a private Jesuit Catholic research university located in the affluent village of Chestnut Hill, Massachusetts, United States, 6 miles (9.7 km) west of Boston. The university has more than 9,300 full-time undergraduates and nearly 5,000 graduate students. The university's name reflects its early history as a liberal arts college and preparatory school (now Boston College High School) in Dorchester. It is a member of the 568 Group and the Association of Jesuit Colleges and Universities. Its main campus is a historic district and features some of the earliest examples of collegiate gothic architecture in North America.

Boston College offers bachelor's degrees, master's degrees, and doctoral degrees through its nine schools and colleges: Morrissey College of Arts & Sciences, Boston College Graduate School of Arts & Sciences, Carroll School of Management, Lynch School of Education, Connell School of Nursing, Boston College Graduate School of Social Work, Boston College Law School, Boston College School of Theology and Ministry, Woods College of Advancing Studies. In 2018, Boston College was ranked America's 50th top college by Forbes.[4] According to U.S. News & World Report, the school tied as the 38th best national school.[5]

Boston College athletic teams are known as the Eagles, their colors are maroon and gold, and mascot is Baldwin the Eagle. The Eagles compete in NCAA Division I as members of the Atlantic Coast Conference in all sports offered by the ACC. The men's and women's ice hockey teams compete in Hockey East. Boston College's men's ice hockey team has won five national championships.[6]
"""
score2 = SentimentIntensityAnalyzer().polarity_scores(sentence2)
print(score2)

sentence3= """
Bentley University is a private co-educational university in Waltham, Massachusetts, 9 miles (14 km) west of Boston, focused on business. Founded in 1917 as a school of accounting and finance in Boston's Back Bay neighborhood, Bentley moved to Waltham in 1968. Bentley awards bachelor of science degrees in 14 business fields and bachelor of arts degrees in 11 arts and sciences disciplines, offering 36 minors spanning both arts and science and business disciplines. The graduate school emphasizes the impact of technology on business practice, and offers PhD programs in Business and Accountancy, the Bentley MBA with 16 areas of concentration, an integrated MS+MBA, seven Master of Science degrees, several graduate certificate programs and custom executive education programs.

Bentley's athletic teams compete in Division II of the NCAA (except for men's hockey, which competes in Division I) and is known collectively as the Bentley Falcons
"""

score3 = SentimentIntensityAnalyzer().polarity_scores(sentence3)
print(score3)
