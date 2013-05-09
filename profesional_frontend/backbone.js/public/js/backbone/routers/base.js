Puls3.Routers.BaseRouter = Backbone.Router.extend({
	routes: {
		"" :  "root",
    "article/:id" : "articleSingle"
	},
	initialize : function(){
		var self = this;

	},
	root: function(){
		var self = this;

    console.log('root');
    $("#contenido > div").show();
	},
	articleSingle: function(id){
    console.log('ArticleSingle', id);
    $("#contenido > div").hide();
    $("#contenido #" + id).show();
	}
});
