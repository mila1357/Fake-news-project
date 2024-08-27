chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.create({
    url: chrome.extension.getURL('templates/popup.html'),
    active: true
  });
});