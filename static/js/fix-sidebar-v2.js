(function($) {
  'use strict';

  console.log("Fix Sidebar V2 Loaded");

  function enforceLayout() {
      // CRITICAL FIX: Reset body horizontal scroll to 0
      // Theme JS sets body.scrollLeft = 20 on taxonomy pages, causing -20px layout shift
      document.body.scrollLeft = 0;
      document.documentElement.scrollLeft = 0;
      window.scrollTo(0, window.scrollY); // Reset horizontal scroll without affecting vertical

      const $sidebar = $('#sidebar');
      const $blog = $('#blog');
      const $main = $('#main');
      const $headerTitle = $('.header-title');
      const $bottomBar = $('#bottom-bar');
      const $postHeader = $('.post-header-cover');

      // 1. Force Sidebar
      if ($sidebar.length) {
          $sidebar[0].style.setProperty('left', '0', 'important');
          $sidebar[0].style.setProperty('display', 'block', 'important');
          $sidebar[0].style.setProperty('transform', 'none', 'important');
          
          // Ensure it has the class
          if (!$sidebar.hasClass('pushed')) $sidebar.addClass('pushed');
      }

      // 2. Force Content Elements
      const contentElements = [
          $main[0], 
          $headerTitle[0], 
          $bottomBar[0],
          $postHeader[0]
      ];

      contentElements.forEach(function(el) {
          if (el) {
              el.style.setProperty('margin-left', '250px', 'important');
              el.style.setProperty('width', 'calc(100% - 250px)', 'important');
              el.style.setProperty('transform', 'none', 'important');
              el.style.setProperty('transition', 'none', 'important');
              
              if (el.id === 'main') {
                  el.style.setProperty('background-color', '#fff', 'important');
                  el.style.setProperty('min-height', '100vh', 'important');
              }
          }
      });

      // 3. Force Wrapper Class
      if ($blog.length && !$blog.hasClass('pushed')) {
          $blog.addClass('pushed');
      }
  }

  $(document).ready(function() {
      // Immediate Run
      enforceLayout();

      // Mutation Observer (The primary guard)
      const observer = new MutationObserver(function(mutations) {
          // Debounce slightly or just run
          // We'll run immediately but safeguard against our own changes?
          // Since we check if values (like classes) are missing before adding, it should be fine.
          // For styles, we blindly set !important.
          enforceLayout();
      });

      const targets = [
          document.getElementById('main'),
          document.getElementById('sidebar'),
          document.getElementById('blog')
      ];

      targets.forEach(function(target) {
          if (target) {
              observer.observe(target, { 
                  attributes: true, 
                  attributeFilter: ['style', 'class'] 
              });
          }
      });

      // Failsafe Interval (The backup guard)
      // Checks every 500ms to ensure no long-running animations or delayed scripts broke layout
      setInterval(enforceLayout, 500);

      // Window Resize
      $(window).on('resize', enforceLayout);
  });

})(jQuery);
