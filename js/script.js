document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const burgerBtn = document.querySelector('.burger');
  const mainNav = document.querySelector('.main-nav');
  const body = document.body;

  if (burgerBtn && mainNav) {
    burgerBtn.addEventListener('click', () => {
      const isActive = mainNav.classList.toggle('mobile-active');
      body.classList.toggle('menu-open', isActive);
      
      if (isActive) {
        // Change to X
        burgerBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>';
      } else {
        // Change to Hamburger
        burgerBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>';
      }
    });
  }

  // Category Filter Pills Toggle
  const categoryPills = document.querySelectorAll('.cat-pill');
  categoryPills.forEach(pill => {
    pill.addEventListener('click', () => {
      // Remove active class from all
      categoryPills.forEach(p => p.classList.remove('active'));
      // Add active class to clicked pill
      pill.classList.add('active');
    });
  });

  // Favorite Buttons Toggle
  const favBtns = document.querySelectorAll('.fav-btn');
  favBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault(); // Prevent navigating if wrapped in a tag later
      e.stopPropagation();
      btn.classList.toggle('liked');
    });
  });

  // Pagination Toggle
  const pageNums = document.querySelectorAll('.page-num');
  pageNums.forEach(num => {
    num.addEventListener('click', () => {
      pageNums.forEach(p => p.classList.remove('active'));
      num.classList.add('active');
    });
  });

  // Mobile Advanced Carousel Navigation
  const setupRowScroll = (prevCls, nextCls, rowCls) => {
    const prevBtn = document.querySelector(prevCls);
    const nextBtn = document.querySelector(nextCls);
    const row = document.querySelector(rowCls);

    if (prevBtn && nextBtn && row) {
      prevBtn.addEventListener('click', () => {
        const card = row.querySelector('.product-card');
        if(card) {
          row.scrollBy({ left: -(card.offsetWidth + 12), behavior: 'smooth' });
        }
      });
      
      nextBtn.addEventListener('click', () => {
        const card = row.querySelector('.product-card');
        if(card) {
          row.scrollBy({ left: card.offsetWidth + 12, behavior: 'smooth' });
        }
      });
    }
  };

  setupRowScroll('.nav-prev-1', '.nav-next-1', '.row-1');
  setupRowScroll('.nav-prev-2', '.nav-next-2', '.row-2');

  setupRowScroll('.nav-prev-3', '.nav-next-3', '.row-3');
  setupRowScroll('.nav-prev-4', '.nav-next-4', '.row-4');


  // FAQ Accordion Toggle
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (question) {
      question.addEventListener('click', () => {
        item.classList.toggle('active');
        const answer = item.querySelector('.faq-answer');
        if (item.classList.contains('active')) {
          answer.style.display = 'block';
        } else {
          answer.style.display = 'none';
        }
      });
    }
  });
});
