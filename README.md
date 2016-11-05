# cz3003ssadBack

Data from Front End

https://gist.github.com/joetancy/ef35fbe72512509e5708e91e0936f620

All API calls will be in the Django development server
127.0.0.1:800/<API-HERE>

**submitCrisis**

* Takes in JSON format, returns JSON received

**approveCrisis/cid**

* Takes in crisis ID, change attribute 'approved' to True.
* Returns approved crisis

**closeCrisis/cid**

* Takes in crisis ID(int), change attribute 'closed' to True.
* Returns closed crisis

**getApprovedCrisis**

* Returns all crisis where attribute 'approved' = True in JSON format

**getUnapprovedCrisis**

* Returns all crisis where attribute 'approved' = False in JSON format

**sendDispatch/cid/dispatcher**

* Takes in crisis ID(int) and dispatcher(string), creates new row in
Dispatch and send out SMS with the corresponding crisis details.
* Returns Dispatch data

**toggleCrisisModeOn**

* Creates a new row in CrisisMode with attribute 'inCrisis' = True with current datetime.
* Returns newly created CrisisMode

**toggleCrisisModeOff**

* Creates a new row in CrisisMode with attribute 'inCrisis' = False with current datetime.
* Returns newly created CrisisMode

**sendToTwitter/cid**

* Sends a tweet to twitter with details of the corresponding crisis where crisis_id = cid
* Returns corresponding crisis

**sendToFacebook/cid**

* Post to Facebook with details of the corresponding crisis where crisis_id = cid
* Returns corresponding crisis
