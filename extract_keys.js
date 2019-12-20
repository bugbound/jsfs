var __webnuke_collectedData = [];
var __webnuke_collectedProps = [];
var __webnuke_collectedFuncs = [];
var __webnuke_collectedFiles = [];
var __webnuke_shitlist=[ 'postMessage', 'blur', 'focus', 'close', 'parent', 'opener', 'top', 'length', 
					   'frames', 'closed', 'self', 'window', 'document', 'customElements', 
					   'history', 'locationbar', 'menubar', 'personalbar', 'scrollbars', 'statusbar', 'toolbar', 
					   'frameElement', 'navigator', 'origin', 'external', 'screen', 'innerWidth', 
					   'innerHeight', 'scrollX', 'pageXOffset', 'scrollY', 'pageYOffset', 'visualViewport', 
					   'screenX', 'screenY', 'outerWidth', 'outerHeight', 'devicePixelRatio', 'clientInformation', 
					   'screenLeft', 'screenTop', 'defaultStatus', 'defaultstatus', 'styleMedia', 'onanimationend', 
					   'onanimationiteration', 'onanimationstart', 'onsearch', 'ontransitionend', 'onwebkitanimationend', 
					   'onwebkitanimationiteration', 'onwebkitanimationstart', 'onwebkittransitionend', 'isSecureContext', 
					   'onabort', 'onblur', 'oncancel', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick', 'onclose', 
					   'oncontextmenu', 'oncuechange', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 
					   'ondragover', 'ondragstart', 'ondrop', 'ondurationchange', 'onemptied', 'onended', 'onerror', 
					   'onfocus', 'oninput', 'oninvalid', 'onkeydown', 'onkeypress', 'onkeyup', 'onload', 
					   'onloadeddata', 'onloadedmetadata', 'onloadstart', 'onmousedown', 'onmouseenter', 
					   'onmouseleave', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel', 
					   'onpause', 'onplay', 'onplaying', 'onprogress', 'onratechange', 'onreset', 'onresize', 
					   'onscroll', 'onseeked', 'onseeking', 'onselect', 'onstalled', 'onsubmit', 'onsuspend', 
					   'ontimeupdate', 'ontoggle', 'onvolumechange', 'onwaiting', 'onwheel', 'onauxclick', 
					   'ongotpointercapture', 'onlostpointercapture', 'onpointerdown', 'onpointermove', 
					   'onpointerup', 'onpointercancel', 'onpointerover', 'onpointerout', 'onpointerenter', 
					   'onpointerleave', 'onselectstart', 'onselectionchange', 'onafterprint', 'onbeforeprint', 
					   'onbeforeunload', 'onhashchange', 'onlanguagechange', 'onmessage', 'onmessageerror', 
					   'onoffline', 'ononline', 'onpagehide', 'onpageshow', 'onpopstate', 'onrejectionhandled', 
					   'onstorage', 'onunhandledrejection', 'onunload', 'performance', 'stop', 'open', 'alert', 
					   'confirm', 'prompt', 'print', 'queueMicrotask', 'requestAnimationFrame', 'cancelAnimationFrame', 
					   'captureEvents', 'releaseEvents', 'requestIdleCallback', 'cancelIdleCallback', 'getComputedStyle', 
					   'matchMedia', 'moveTo', 'moveBy', 'resizeTo', 'resizeBy', 'scroll', 'scrollTo', 'scrollBy', 
					   'getSelection', 'find', 'webkitRequestAnimationFrame', 'webkitCancelAnimationFrame', 'fetch', 
					   'btoa', 'atob', 'setTimeout', 'clearTimeout', 'setInterval', 'clearInterval', 'createImageBitmap', 
					   'onappinstalled', 'onbeforeinstallprompt', 'crypto', 'indexedDB', 'webkitStorageInfo', 
					   'chrome', 'onformdata', 'onpointerrawupdate', 'speechSynthesis', 
					   'webkitRequestFileSystem', 'webkitResolveLocalFileSystemURL', 'openDatabase', 'replace', 'href', 
					   'ancestorOrigins', 'protocol', 'port', 'pathname', 'search', 'hash', 
					   'assign', 'reload', 'toString', '$cdc_asdjflasutopfhvcZLmcfl_', 'loadTimes', 
					   'csi', 'app', 'cache_', 'isInstalled', 'getDetails', 'getIsInstalled', 'installState', 
					   'runningState', 'InstallState', 'RunningState', 'addEventListener', 'removeEventListener', 'dispatchEvent',
					   'TEMPORARY', 'PERSISTENT', 'ondevicemotion', 'ondeviceorientation', 'ondeviceorientationabsolute'];



window.__webnuke_collectKeys = function (obj)
{
	for( var key in obj ) 
	{
		// ignore any of our programs custom functions...
		if(key.startsWith('__webnuke') == false)
		{
			// check if default stuff
			if(__webnuke_shitlist.indexOf(key) == -1)
			{				
				if ( typeof obj[key] === 'object' )
				{
					__webnuke_collectedProps.push(key+"/")
				}
				
				if ( typeof obj[key] === 'function' )
				{
					__webnuke_collectedFuncs.push(key)
				}
				
				if ( typeof obj[key] === 'string' || typeof obj[key] === 'number' || typeof obj[key] === 'boolean' )
				{
					__webnuke_collectedFiles.push(key)
				}
				
				
				
				if ( obj.hasOwnProperty(key) ) 
				{
					// if we dont know about it, add it to our list
					if(__webnuke_collectedData.indexOf(key) == -1)
					{
						__webnuke_collectedData.push(key);
					}
				
				}
			}
		}
	}
}

window.__webnuke_run_collector = function(rootObj)
{
	__webnuke_collectKeys(rootObj);
	return {'data': __webnuke_collectedData, 'props': __webnuke_collectedProps, 'funcs': __webnuke_collectedFuncs, 'files': __webnuke_collectedFiles};
}
