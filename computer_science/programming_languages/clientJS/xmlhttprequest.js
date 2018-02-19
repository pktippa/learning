// URL want to hit
var url = 'http://localhost:8084/v1'
// Opening up new XMLHttpRequest
var http = new XMLHttpRequest()
// Making a POST request
http.open('POST',url, true)
// Setting up Request headers
http.setRequestHeader("Content-type","application/json")
// Constructing POST data
data = '{"id": "abcd"}'
// Sending the POST data
http.send(data)
// On ready state
http.onreadystatechange = function() {//Call a function when the state changes.
    // Checking the readystate is when the HEADERS are recieved
    if(http.readyState == http.HEADERS_RECEIVED) {
        // Alerting the particular header from the object
        alert(http.getResponseHeader("token"));
    }
}
