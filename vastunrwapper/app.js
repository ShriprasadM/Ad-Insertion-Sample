const vastLibrary = require('vast-client')
const vastClient = new vastLibrary.VASTClient();
const vastParser = new vastLibrary.VASTParser();
const express = require('express')
var bodyParser = require('body-parser')
var HTTPStatus =require('http-status');

const app = express()
const port = 3000
app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json())
app.get('/', (req, res) => res.send('Hello World!'))

app.post('/api/unwrapVast', function (req, res) {
    try {
        console.log("Request is" + req.body);
        console.log('Applying : VAST Unwrapping', req.body.adm);
        vastXmlString = req.body.adm;
        var vastJsonResp = {};
        if (vastXmlString.startsWith('http') || vastXmlString.startsWith('https')) {
            vastJsonResp = vastClient.get(vastXmlString).then(function (parsedXML) {
                console.log('JSON : ', parsedXML);
                res.status(HTTPStatus.OK).send(parsedXML);
            }).catch(function(error){
                res.status(HTTPStatus.BAD_REQUEST).send('Please check the vast url' + JSON.stringify(error));
            });
        } else {
            vastJsonResp = vastParser.parseVAST(vastXmlString).then(function (parsedXML) {
                console.log('JSON : ', parsedXML);
                res.status(HTTPStatus.OK).send(parsedXML);
            }).catch(function(error){
                res.status(HTTPStatus.BAD_REQUEST).send('Please check the vast url' + JSON.stringify(error));             
            });
        }
    } catch (ex) {
        console.log("Exceptions is ", ex);
    }
})

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))