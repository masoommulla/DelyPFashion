document.addEventListener("DOMContentLoaded", () => {
  // Ensure GSAP and ScrollTrigger are loaded
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

  gsap.registerPlugin(ScrollTrigger);

  // 1. Hero Section Initial Animation
  const heroTl = gsap.timeline();
  
  // Header slides down
  heroTl.from(".site-header", {
    y: -100,
    opacity: 0,
    duration: 0.8,
    ease: "power3.out"
  })
  // Title slides up
  .from(".hero-content h1", {
    y: 50,
    opacity: 0,
    duration: 0.8,
    ease: "power3.out"
  }, "-=0.4")
  // Subtitle and CTA slide up
  .from(".hero-content p, .hero-content .btn-primary", {
    y: 30,
    opacity: 0,
    duration: 0.6,
    stagger: 0.2,
    ease: "power2.out"
  }, "-=0.6");

  // 2. Scroll Animations

  // Batch Category Cards
  ScrollTrigger.batch(".category-card", {
    onEnter: batch => gsap.fromTo(batch, 
      { opacity: 0, y: 50, scale: 0.95 },
      { opacity: 1, y: 0, scale: 1, stagger: 0.15, duration: 0.8, ease: "power2.out", overwrite: true }
    ),
    start: "top 85%",
    once: true
  });

  // Batch Product Cards
  ScrollTrigger.batch(".product-card", {
    onEnter: batch => gsap.fromTo(batch,
      { opacity: 0, y: 40 },
      { opacity: 1, y: 0, stagger: 0.1, duration: 0.6, ease: "power2.out", overwrite: true }
    ),
    start: "top 85%",
    once: true
  });

  // Fade up Feature Text Blocks (e.g. Materials/Craft)
  gsap.utils.toArray(".materials-craft-content, .featured-content, .content-block").forEach(block => {
    gsap.from(block, {
      scrollTrigger: {
        trigger: block,
        start: "top 80%",
        once: true
      },
      opacity: 0,
      y: 40,
      duration: 1,
      ease: "power3.out"
    });
  });

  // Parallax for large images
  gsap.utils.toArray(".materials-craft-img img, .featured-image img, .grid-item img").forEach(img => {
    gsap.from(img, {
      scrollTrigger: {
        trigger: img.parentElement,
        start: "top bottom",
        end: "bottom top",
        scrub: true
      },
      y: 50,
      scale: 1.1,
      ease: "none"
    });
  });

  // Footer Fade Up
  gsap.from(".site-footer", {
    scrollTrigger: {
      trigger: ".site-footer",
      start: "top 95%",
      once: true
    },
    opacity: 0,
    y: 50,
    duration: 0.8,
    ease: "power2.out"
  });

});
