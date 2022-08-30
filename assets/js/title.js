/*
  -------------------------------------------------------------
  Pranjal Pathak Portfolio hosted on GitHub, Inc.
  
  GNU GENERAL PUBLIC LICENSE
  Version 3, 29 June 2007
  Copyright (C). 2007 Free Software Foundation, Inc.
  -------------------------------------------------------------
*/

// Title-scrambler
function ts(phrases, css_element) {

    class TextScramble {
      constructor(el) {
        this.el = el;
        this.chars = "!<>-_\\/[]{}—=+*^?#________";
        this.update = this.update.bind(this);
      }
      setText(newText) {
        const oldText = this.el.innerText;
        const length = Math.max(oldText.length, newText.length);
        const promise = new Promise((resolve) => (this.resolve = resolve));
        this.queue = [];
        for (let i = 0; i < length; i++) {
          const from = oldText[i] || "";
          const to = newText[i] || "";
          const start = Math.floor(Math.random() * 40);
          const end = start + Math.floor(Math.random() * 40);
          this.queue.push({ from, to, start, end });
        }
        cancelAnimationFrame(this.frameRequest);
        this.frame = 0;
        this.update();
        return promise;
      }
      update() {
        let output = "";
        let complete = 0;
        for (let i = 0, n = this.queue.length; i < n; i++) {
          let { from, to, start, end, char } = this.queue[i];
          if (this.frame >= end) {
            complete++;
            output += to;
          } else if (this.frame >= start) {
            if (!char || Math.random() < 0.28) {
              char = this.randomChar();
              this.queue[i].char = char;
            }
            output += `<span class="dud">${char}</span>`;
          } else {
            output += from;
          }
        }
        this.el.innerHTML = output;
        if (complete === this.queue.length) {
          this.resolve();
        } else {
          this.frameRequest = requestAnimationFrame(this.update);
          this.frame++;
        }
      }
      randomChar() {
        return this.chars[Math.floor(Math.random() * this.chars.length)];
      }
    }

    const el = document.querySelector(css_element);
    const fx = new TextScramble(el);
    const next = () => {
      fx.setText(phrases[0]).then(() => {
      });
    };

    next();
}


// .title-contained-text
var scrolled = false;
$(window).scroll(function() {
   var hT = $('#titler1').offset().top,
       wH = $(window).height(),
       wS = $(this).scrollTop();
   if (wS > (hT-wH) && scrolled == false){
       console.log('H1 on the view!');
       ts(["About Me"], ".title-contained-text");
       scrolled=true;
   }
});

// .title-contained-text-2
var scrolled2 = false;
$(window).scroll(function() {
   var hT = $('#titler').offset().top,
       wH = $(window).height(),
       wS = $(this).scrollTop();
   if (wS > (hT-wH) && scrolled2 == false){
       console.log('H1 on the view!');
       ts(["My Resume"], ".title-contained-text-2");
       scrolled2=true;
   }
});