$(document).ready(function(){
	console.log('Starting app');

  window.collections.articles = new Puls3.Collections.ArticlesCollection();
  window.routers.base = new Puls3.Routers.BaseRouter();
  
  window.collections.articles.on('add', function(model){
    var view = new Puls3.Views.ArticleView(model);
    
    view.render();

    view.$el.insertAfter('#contenido aside');
  });

  var xhr = $.get('/articles/all');
  xhr.done(function(data){
    data.forEach(function(item){
      window.collections.articles.add(item);
    });

    Backbone.history.start({
      root : "/",
      pushState : true,
      silent : false
    });
       
  });

  $('nav li:first').on('click', function(){
      Backbone.history.navigate('', {trigger: true})
  });
  
  $('#header_logo').on('click', function(){
      Backbone.history.navigate('', {trigger: true})
  });
});
