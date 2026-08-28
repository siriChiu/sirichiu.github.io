// Resume popup functionality - similar to About popup
(function($) {
    "use strict";
    
    function ResumePopup() {
        this.$openBtn = $("#sidebar, #header").find("a[href*='#resume']");
        this.$closeBtn = $("#resume-btn-close");
        this.$blog = $("#blog");
        this.$resume = $("#resume");
        this.$resumeCard = $("#resume-card");
    }
    
    ResumePopup.prototype = {
        run: function() {
            var self = this;
            
            self.$openBtn.click(function(e) {
                e.preventDefault();
                self.play();
            });
            
            self.$closeBtn.click(function(e) {
                e.preventDefault();
                self.playBack();
            });
            
            self.$resume.click(function(e) {
                if (e.target === this) {
                    e.preventDefault();
                    self.playBack();
                }
            });
            
            self.$resumeCard.click(function(e) {
                e.stopPropagation();
            });
        },
        
        play: function() {
            var self = this;
            self.$blog.fadeOut();
            self.$resume.fadeIn();
            setTimeout(function() {
                self.dropResumeCard();
            }, 300);
        },
        
        playBack: function() {
            var self = this;
            self.liftResumeCard();
            setTimeout(function() {
                self.$blog.fadeIn();
            }, 500);
            setTimeout(function() {
                self.$resume.fadeOut();
            }, 500);
        },
        
        dropResumeCard: function() {
            var self = this;
            var cardHeight = self.$resumeCard.innerHeight();
            var windowHeight = $(window).height();
            var endPos = windowHeight / 2 - cardHeight / 2 + cardHeight;
            
            if (cardHeight + 30 > windowHeight) {
                endPos = cardHeight;
            }
            
            self.$resumeCard
                .css("top", "0px")
                .css("top", "-" + cardHeight + "px")
                .show(500, function() {
                    self.$resumeCard.animate({
                        top: "+=" + endPos + "px"
                    });
                });
        },
        
        liftResumeCard: function() {
            var self = this;
            var cardHeight = self.$resumeCard.innerHeight();
            var windowHeight = $(window).height();
            var endPos = windowHeight / 2 - cardHeight / 2 + cardHeight;
            
            if (cardHeight + 30 > windowHeight) {
                endPos = cardHeight;
            }
            
            self.$resumeCard.animate({
                top: "-=" + endPos + "px"
            }, 500, function() {
                self.$resumeCard.hide();
                self.$resumeCard.removeAttr("style");
            });
        }
    };
    
    $(document).ready(function() {
        new ResumePopup().run();
    });
    
})(jQuery);
