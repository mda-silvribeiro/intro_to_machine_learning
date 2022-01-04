# Naive Bayes
<p> Naive Bayesian Algorithms are powerful tool for creating classifiers for<br>
incoming labeled data. Specifically Naive Bayes is frequently used with data <br>
and classification problems</p>

<h1> <b>Application Bayes Theorem </b></h1>
<p> 99% accuracy 1 out 10.000 people are sick</p>
<h4> Information </h4>
<li>
    <ul> S = Sick</ul>
    <ul> H = Healthy</ul>
    <ul> + = Positive</ul>
</li>
<h4> Application </h4>
<li>
    <ul> P(S) = 0.0001 </ul>
    <ul> P(H) = 0.9999</ul>
    <ul> P(+|S) = 0.99</ul>
    <ul> P(+|H) = 0.01</ul>
</li>
<p><b>
               
P(S|+)  =  P(S) P(+ | S) / P(S) P(+ | S) + P(H) P(+ | H) 
        = 0.0001 * 0.99 / 0.0001 * 0.99 + 0.9999 * 0.01
        = 0.0098
        < 1%  
</b></p>

# Bayesian Learning
<div>
    <p> How do we use this wonderful Bayes Theorem to do machine learning?</p>
    <h3> example <b>spam email</b><h3>
    <img style="width:auto;" src="img/spam_easy.png" alt="spam_easy">
    <img style="width:auto;" src="img/spam_money.png" alt="spam_money">
</div>

# Naive Bayes Algorithm
<div>
    <img style="width:auto;" src="img/naive1.png" alt="naive1">
    <img style="width:auto;" src="img/naive2.png" alt="naive2">
    <img style="width:auto;" src="img/naive3.png" alt="naive3">
    <img style="width:auto;" src="img/naive4.png" alt="naive4">
</div>
