var onDisconnected = function() {
    console.log("disconnected");
}

var onNativeMessage = function(msg) {
    console.log("got msg: " + msg)
}


function connect() {
    port = chrome.runtime.connectNative('sendlinux');
    port.onMessage.addListener(onNativeMessage);
    port.onDisconnect.addListener(onDisconnected);
}

chrome.runtime.onMessage.addListener(function(data, sender) {
    console.log("got msg: " + data);
    if (data.length > 0) {
        //connect();
        chrome.runtime.sendNativeMessage('sendlinux',
            { text: " https://www.youtube.com/watch?v=0b46E4mp_V8i"},
            function(response) {
                console.log("Received " + response);
            });
    }
});

/*
 *
 *var port = chrome.runtime.connectNative('mpv');
 *port.onMessage.addListener(function(msg) {
 *  console.log("Received" + msg);
 *});
 *port.onDisconnect.addListener(function() {
 *  console.log("Disconnected");
 *});
 *port.postMessage({ text: " https://www.youtube.com/watch?v=y3h02BDPMJw" });
 */