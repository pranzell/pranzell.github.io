/*
	-------------------------------------------------------------
	Pranjal Pathak Portfolio hosted on GitHub, Inc.
	
	GNU GENERAL PUBLIC LICENSE
	Version 3, 29 June 2007
	Copyright (C). 2007 Free Software Foundation, Inc.
	-------------------------------------------------------------
*/

/* Function for Scroll view elements */


// Skill-mf-Bar.
  const observer1 = new IntersectionObserver(entries => {
    
    // Loop over the entries
    entries.forEach(entry => {
      const square1 = entry.target.querySelector('.pb1');
      const square2 = entry.target.querySelector('.pb2');
      const square3 = entry.target.querySelector('.pb3');
      const square4 = entry.target.querySelector('.pb4');

      if (entry.isIntersecting) {
        square1.classList.add('progress-bar-animation1');
        square2.classList.add('progress-bar-animation2');
        square3.classList.add('progress-bar-animation3');
        square4.classList.add('progress-bar-animation4');
  	  return;
      }

      // We're not intersecting, so remove the class!
      square1.classList.remove('progress-bar-animation1');
      square2.classList.remove('progress-bar-animation2');
      square3.classList.remove('progress-bar-animation3');
      square4.classList.remove('progress-bar-animation4');
    });

  });

  // One target:
  //const target2 = document.querySelector('.timeline-animation-wrapper1');
  //observer2.observe(target2);

  // Iterate over all items in Observer tracker
  let target1 = '.progress-bar-wrapper';
  document.querySelectorAll(target1).forEach((i) => {
      if (i) {
          observer1.observe(i);
      }
  });


// Timeline.
  const observer2 = new IntersectionObserver(entries => {
    
    // Loop over the entries
    entries.forEach(entry => {
      const ab1 = entry.target.querySelector('.ab1');
      const ab2 = entry.target.querySelector('.ab2');
      const ab3 = entry.target.querySelector('.ab3');
      const ab4 = entry.target.querySelector('.ab4');
      const ab5 = entry.target.querySelector('.ab5');
      const ab6 = entry.target.querySelector('.ab6');
      const ab7 = entry.target.querySelector('.ab7');

      if (entry.isIntersecting) {
        ab1.classList.add('animate-box1');
        ab2.classList.add('animate-box2');
        ab3.classList.add('animate-box3');
        ab4.classList.add('animate-box4');
        ab5.classList.add('animate-box5');
        ab6.classList.add('animate-box6');
        ab7.classList.add('animate-box7');
        // stop after one run
        observer2.unobserve(entry.target);
  	  return;
      }

      // We're not intersecting, so remove the class!
      ab1.classList.remove('animate-box1');
      ab2.classList.remove('animate-box2');
      ab3.classList.remove('animate-box3');
      ab4.classList.remove('animate-box4');
      ab5.classList.remove('animate-box5');
      ab6.classList.remove('animate-box6');
      ab7.classList.remove('animate-box7');
      
    });

  });

  // Iterate over all items in Observer tracker
  let target2 = '.timeline-animation-wrapper';
  document.querySelectorAll(target2).forEach((i) => {
      if (i) {
          observer2.observe(i);
      }
  });


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
     var hT = $('#title-about-me').offset().top,
         wH = $(window).height(),
         wS = $(this).scrollTop();
     if (wS > (hT-wH) && scrolled == false){
         // console.log('on the view!');
         ts(["About Me"], ".title-contained-text");
         scrolled=true;
     }
  });

  // .title-contained-text-2
  var scrolled2 = false;
  $(window).scroll(function() {
     var hT = $('#title-resume').offset().top,
         wH = $(window).height(),
         wS = $(this).scrollTop();
     if (wS > (hT-wH) && scrolled2 == false){
         ts(["My Resume"], ".title-contained-text-2");
         scrolled2=true;
     }
  });

  // .title-contained-text-3
  var scrolled3 = false;
  $(window).scroll(function() {
     var hT = $('#title-touchbase').offset().top,
         wH = $(window).height(),
         wS = $(this).scrollTop();
     if (wS > (hT-wH) && scrolled3 == false){
         ts(["Get in touch"], ".title-contained-text-3");
         scrolled3=true;
     }
  });


// Timeline Icon swiggler
  