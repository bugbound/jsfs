window.__webnuke_getAngularAllClasses = function(){
	var deps = __webnuke_getAllAngularDeps();
	var rtnData = [];
	angular.forEach(deps, function(m){
		var namespace_classes = __webnuke_getAngularClasses(m['namespace']);
		rtnData.push({'namespace': m['namespace'], 'classes': namespace_classes});
	
	});
	return rtnData;
};


window.__webnuke_getAngularClasses = function(namespace){
	//namespace = 'angularFlaskServices';
	//namespace = 'reporterApp';
	var rtnData = [];
	angular.module(namespace)['_invokeQueue'].forEach(function(value){ 
		var items = value[2][1];
		var isarray = items instanceof Array;
		var item_name = value[2][0];
		if(isarray){
			var components = items.slice(0, -1);
			var source = items[items.length-1];
			var record = {'type': value[1], 'name': value[2][0], 'sourcecode': source, 'components': components}
			rtnData.push(record);
		}
		else{
			var source = "na";
			var components = value[2][1]
			var record = {'type': value[1], 'name': value[2][0], 'sourcecode': source, 'components': components};
			rtnData.push(record);
		}								
	});
	return rtnData;
};

window.__webnuke_getAngularAppName = function(){
	if(typeof angular !== 'undefined'){
		var appname = '';
		var rootelement = angular.element(document.body).injector().get('$rootElement');
		if(rootelement && rootelement.attr('ng-app')) {
			appname = rootelement.attr('ng-app');
		}
		if(rootelement && rootelement.attr('data-ng-app')) {
			appname = rootelement.attr('data-ng-app');
		}
		return appname;
	}
	return "No AngularJS app found."
	
};

window.__webnuke_getAllAngularDeps = function(namespace){
	var main_app_name = __webnuke_getAngularAppName();
	var deps_list=[];
	var main_deps = __webnuke_getAngularDeps(main_app_name);
	deps_list.push({'namespace': main_app_name, 'deps': main_deps});
	
	if(typeof angular !== 'undefined'){
		angular.forEach(main_deps, function(m){
			var deps = __webnuke_getAngularDeps(m);
			deps_list.push({'namespace': m, 'deps': deps});
		});
		
		//now get remaining namespaces....
		var additional_namespaces=[]
		angular.forEach(deps_list, function(m){
			var deps = m['deps'];
			angular.forEach(deps, function(depname){
				if(__webnuke_contains_namespace(depname, deps_list)==false){
					additional_namespaces.push(depname);
				}
			});
		});
		
		angular.forEach(additional_namespaces, function(m){
			var deps = __webnuke_getAngularDeps(m);
			deps_list.push({'namespace': m, 'deps': deps});
		});
	}
	return deps_list;
};


window.__webnuke_getAngularDeps = function(namespace){
	var deps = [];
	if(typeof angular !== 'undefined'){
		angular.forEach(angular.module(namespace).requires, function(m){deps.push(m);});
	}
	return deps;
};


window.__webnuke_contains_namespace = function(namespace, alldeps){
	angular.forEach(alldeps, function(m){
		if(m['namespace'] == namespace){
			return true;
		}
	});
	
	return false;
};


window.__webnuke_getNgResourceClasses = function(){
	var resource_classes = [];
	var deps = __webnuke_getAllAngularDeps();
	
	if(typeof angular !== 'undefined'){
		angular.forEach(deps, function(m){
			var contains_ngresource = false;
			angular.forEach(m['deps'], function(mm){
				if(mm == 'ngResource'){
					var namespace = m['namespace']
					
					var angular_classes = __webnuke_getAngularClasses(namespace);
					angular.forEach(angular_classes, function(angular_classname){
						resource_classes.push(angular_classname['name']);
					});
				}
			});
		});
	}
	return resource_classes;
};




window.__webnuke_run_discovery = function(){
	var angular_classes = __webnuke_getNgResourceClasses();
	return angular_classes;
}
