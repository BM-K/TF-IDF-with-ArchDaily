# TF-IDF-with-ArchDaily
I learnd TF-IDF similarlity measure with web page "Arch Daily"

## Motive
I belong to Kyung-Hee university and study Natural Language Processing. 
Recently I read about TF-IDF similarity measure. 
So I want to use it in real life, I applied "https://www.archdaily.com/" web page.

## Requirement
- BeautofulSoup
- pandas
- sklearn

## Python File
First, i have to gather arch daily data. While doing this project, gathering data i essentially study web crawling.
I also studied web crawling with googling. so code can so dirty and complex. Ask to be excused.

'Gather_ArchData' is code for gather data. This code collect each person's art piece title and descripment in arch daily.
<br>An example follows. https://www.archdaily.com/925586/enrico-fermi-school-bdr-bureau <br>
<img src = https://user-images.githubusercontent.com/55969260/65871434-5a014b80-e3b9-11e9-8015-e59f592fea89.png> <br>
// Collect title <br>
<img src =https://user-images.githubusercontent.com/55969260/65871924-689c3280-e3ba-11e9-9ea8-6d5ea2d75059.png> <br>
// Collect descriptions <br> <br>

I used the following code : <br>
<img src = https://user-images.githubusercontent.com/55969260/65871818-325eb300-e3ba-11e9-8d4f-ee8733451af2.png> <br>
<br>
And similarity was analyzed using TF-IDF of the Scikit-learn library 'TfidfVecorizer' <br>
<img src = "https://user-images.githubusercontent.com/55969260/65872583-d563fc80-e3bb-11e9-9662-6531e2cc9d82.png"> <br>
Part of the code. <br>
