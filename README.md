
### 🎃 They there, present Vatsal here. 

I did this challenge as a part of my application for Machine Learning Operations (MLOps) Co-op where I am current doing my co-op at Retail Business Services (a company of Ahold Delhaize USA). 
This README explains what I had to do for the challenge, and acutally, what I did for the challenge is inside 'docs/' folder. 


# RBS Machine Learning E2E Challenge

> Dear amigo, greetings of peace✌!  
>  
> This challenge is an optional opportunity for you to showcase your amazing engineering design skills, in the context of Machine Learning in addition to your interview with us.
>   
> This mini-project should display your thought process when dealing with:  
>
> - Data 
> - ML algorithms
> - Automation Pipelines
> - Open Source Tools
> - Learning

***

> **Important things to know before we get into the details:**
>
> - Not looking for a single solution; there can be multiple correct ways of doing a task.
> - A program can tell a lot about its author; let your personality shine through!
> - Learning through this project is more valuable than finishing it. And incomplete submissions are better than no submissions.
> - Whenever you feel stressed, take a deep breath take a break and come back later. It works :wink:.

***

## Overview

This challenge has 3 sections:

1. Data & ML Model Training/Tuning
2. ML Model Packaging
3. ML Model Deployment

Open source is a blessing from heaven (and the internet); this entire project expects you to employ open source tooling.

The flow would look like:
![Screen Shot 2021-03-07 at 10 08 57 PM](https://user-images.githubusercontent.com/5572332/110269484-d4ac9e00-7f91-11eb-9f8f-b1ae1bc9bc81.png)

***

## Assessment Factors

Let's address the :elephant: in the room: Your submission will be evaluated on the following items:

1. How you prepped your data
2. How you trained/tuned a machine learning model
3. How you packaged the model (will definitely read your dockerfile)
4. How you deployed/served the model.
5. How you used version control (**quick note:** we :heart: source control)
6. Documentation
   - **README file in the `docs/` directory with atleast the following sections**:
     - Overview
     - Data
     - ML Model Training/Tuning
       - Problem chosen
       - Model chosen to solve problem
       - Model training and tuning
       - Model validation
       - Model testing
     - ML Model Packaging Overview
     - ML Model Deployment Overview
     - Resources Used
   - Note that we value quality of documentation over quantity.
7. General integration of end-to-end solution.

Bonus points:  

- :art: - Creativity shown to accomplish tasks (surprise us!)
- :rocket: - Automation of the above tasks -- For example an automation that validates and tests the model after it was trained. You can even use a tool like [Github Action](https://docs.github.com/en/actions) that comes out of the box with your GitHub repo!

***

## Logistics

Good source and version control are highly underrated ethos.

As demonstrated in the following image, we would like you to:

- [ ] Fork this repository on GitHub.
- [ ] Give us [@pablordoricaw](https://github.com/pablordoricaw) and [@rymsi](https://github.com/rymsi) access to your forked private repository.
- [ ] ❗**Do not work on the `main` branch**❗ At least create one secondary branch to work on. Your `main` branch will be used for your submission.
  - We recommend you follow a Git workflow where you have a `develop` branch with your latest developed changes that are merged in from feature branch(es).

### Submission

When you're ready to submit your challenge:

- [ ] Submit a [Pull Request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests) in your forked private with all your changes to the `main` branch **IN YOUR REPO** with us as reviewers.

❗❗❗
**IMPORTANT:** Please make sure the Pull Request is in YOUR private repo to YOUR `main` branch.
❗❗❗

![challenge-github-flow-1](https://user-images.githubusercontent.com/19933411/114570925-3c66a080-9c44-11eb-8dd1-d8814f2060c8.png)

***

## Section 1 : 🔵 **Data & ML Model Training/Tuning** 🔵

You have the freedom to choose one problem from below:

- Semantic Search (e.g: [jina-ai](https://github.com/jina-ai))
- Optical Character Recognition  (e.g: [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR), [EasyOCR](https://github.com/PaddlePaddle/PaddleOCR))
- Open Domain Question Answering (e.g: [BERT QA](https://mccormickml.com/2020/03/10/question-answering-with-a-fine-tuned-BERT/))
- Time Series Forecasting (e.g: [Prophet](https://github.com/facebook/prophet))

❗ **IMPORTANT:** ❗ *We've deliberately given broad domains so that you can find your own comfort level. Feel free to explore problems not mentioned above.*

Once you choose your problem to work on, the next steps are:

- [ ] Find an open source dataset related to the problem you chose (Kaggle datasets are totally admissible). Prepare your data.
- [ ] Create or pick a model and finetune it trained on this dataset using an open source tool.

Search the internet; find and apply knowledge from examples and projects. Using Google productively is a real strength!

## Section 2 : 🟢 **ML Model Packaging** 🟢

Once you feel that your model is _good enough_, package your model and create an API for its inference server.

Do not underestimate this section!

- [ ] Containerize your model with [Docker](https://www.docker.com/101-tutorial).
- [ ] Build an API for your model with [FastAPI](https://fastapi.tiangolo.com/tutorial/) or [Flask](https://testdriven.io/blog/moving-from-flask-to-fastapi/) :wink:.

## Section 3 : 🟡 **ML Model Deployment** 🟡

- [ ] Deploy your API service on [Heroku](https://www.heroku.com/free) or any other free cloud instance
- [ ] Provide us access to test the service.

In case you run into trouble / can't deploy, make sure your API can run locally so that we can test after cloning your repo.

Voila, thats it! No you just have to **follow the submission instructions from above**, and submit it. You're done, and we're mighty impressed!

## Next Steps

Once you submit your challenge. The next step is for you to walk us through your work in a 30 min call.


***

> Now that we've covered everything necessary, we sincerely wish you best of luck, and hope you enjoy working through this challenge.  
>
> We look forward to receiving your submission and having you showcase it to us.
> Note that incomplete submissions are better than no submissions :smile: so you still have something to showcase to us.
>
> We're quite flexible and try to be responsive, so shoot us an email if you have any questions about the challenge and/or need more time.  
>
> Arigato! :wave:
>
>
> - Pablo ([@pablordoricaw](https://github.com/pablordoricaw)) 
> - Junaid ([@rymsi](https://github.com/rymsi))