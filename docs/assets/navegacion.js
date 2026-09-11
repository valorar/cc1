(() => {
  const bar = document.querySelector('.progress span');
  const links = [...document.querySelectorAll('.toc a[href^="#"]')];
  const sections = links.map(link => document.querySelector(link.getAttribute('href'))).filter(Boolean);
  const update = () => {
    const total = document.documentElement.scrollHeight - innerHeight;
    if (bar) bar.style.width = `${total > 0 ? (scrollY / total) * 100 : 0}%`;
    let current = sections[0];
    for (const section of sections) if (section.getBoundingClientRect().top <= 150) current = section;
    links.forEach(link => link.classList.toggle('is-active', current && link.getAttribute('href') === `#${current.id}`));
  };
  addEventListener('scroll', update, { passive: true });
  update();
})();
