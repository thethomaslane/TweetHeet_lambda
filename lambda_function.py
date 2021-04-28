import json
import statistics
import logging
import needle

from sagemaker.model import Model
from sagemaker import image_uris, session


logger = logging.getLogger()
logger.setLevel(logging.INFO)
endpoint_name = "sentiment-classification-model"

def lambda_handler(context,event):
    logger.info("test")
    predictor = loadModel()
    testTweets = get_tweets()
    result = predict(testTweets,predictor)
    response = {'result': result}
    print(response)
    return response

def loadModel():
    xgb_image = image_uris.retrieve("xgboost", region="us-east-2", version="latest")
    print("image")
    pred_model = Model(model_data="s3://tweetheettrainingdata/TweetHeet-clone/Model/TweetHeet-1/data-processor-models/TweetHeet--dpp9-1-30dfc09773614188865f2bd6dd5bb64c4bdd92ff23f04/output/model.tar.gz", image_uri=xgb_image, role="arn:aws:iam::096058833819:role/service-role/AmazonSageMaker-ExecutionRole-20210313T174043")
    print("model")
    predictor = pred_model.deploy(initial_instance_count=1, instance_type='ml.t2.medium')
    print("predictor")
    return predictor
    
def predict(tweets,predictor):
    results = []
    for i in tweets:
        results.append(predictor.predict(i))
    return statistics.mean(results)

def get_tweets():
    get_request()
    send_response()



token = process.env.BEARER_TOKEN; 

endpointUrl = 'https://api.twitter.com/2/tweets/search/recent'

def get_request() {
    params = {
        'query': 'a lang:en -is:retweet -is:reply -has:images -has:links - has:media',
        'max_results': 10,
        'tweet.fields': "text"
    } 
    
    res = await needle('get', endpointUrl, params, { headers: {
        "authorization": `Bearer ${token}`
    }})


    if(res.body):
        console.log(res.body)
        res.body
    else:
        console.log("error")
        throw new Error ('Unsuccessful request')
    
}

def send_response():
    console.log("check")

    try:
        response = await get_request();
        console.log(response.data[0]);
        res.json(response.data[0]);
        writeToCSV(response.data)

    catch(e):
        console.log(e, "error2")
        res.json(e);
    

createCsvWriter = require('csv-writer').createObjectCsvWriter;

def write_to_3(data):
    s3_writer = s3Writer({
      path: 'out.csv',
      header: [
        {id: 'text', title: 'text'}
      ],
      append: true
    })

    output = []
    for (var i = data.length - 1; i >= 0; i--):
        output.push({"text": data[i].text})
    

    s3_writer.writeRecords(output).then(()=> console.log('The CSV file was written successfully'));
    
