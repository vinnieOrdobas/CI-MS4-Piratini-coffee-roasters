// Materialize Objects
$(document).ready(function() {
    $('.dropdown-trigger').dropdown();
    $('.dropdown-trigger-bag').dropdown();
    $('.sidenav').sidenav({
        edge: 'right',
        
    });
    // search form toggle
    $('.search-form').click(function() {
        $('.search-form-wrapper').toggleClass('open');
        $('.search-form-wrapper .search').focus();
        $('html').toggleClass('search-form-open');
      });
      $('[data-toggle=search-form-close]').click(function() {
        $('.search-form-wrapper').removeClass('open');
        $('html').removeClass('search-form-open');
      });
    $('.search-form-wrapper .search').keypress(function( event ) {
      if($(this).val() == "Search") $(this).val("");
    });
  
    $('.search-close').click(function(event) {
      $('.search-form-wrapper').removeClass('open');
      $('html').removeClass('search-form-open');
    });
})