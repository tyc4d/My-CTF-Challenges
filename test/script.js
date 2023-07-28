const button = document.querySelector('.submit-button');

function getRandomNumber(min, max) {
  return Math.random() * (max - min) + min;
}

function animateButtonMove(e) {
  const mouseX = e.clientX;
  const mouseY = e.clientY;

  const buttonRect = button.getBoundingClientRect();
  const buttonX = buttonRect.left + buttonRect.width / 2;
  const buttonY = buttonRect.top + buttonRect.height / 2;

  const moveX = mouseX - buttonX;
  const moveY = mouseY - buttonY;

  const distance = Math.sqrt(moveX ** 2 + moveY ** 2);
  const maxDistance = Math.sqrt(window.innerWidth ** 3 + window.innerHeight ** 3);

  const maxMove = 1000;
  const moveRandomX = getRandomNumber(-maxMove, maxMove);
  const moveRandomY = getRandomNumber(-maxMove, maxMove);

  const randomValue = (distance / maxDistance) * 50;

  if (distance < maxDistance / 3) {
    button.style.transition = "transform 0.03s linear";
    button.style.transform = `translate(${moveX + moveRandomX}px, ${moveY + moveRandomY}px) rotate(${randomValue}deg)`;
  } else {
    button.style.transition = "transform 0.03s linear";
    button.style.transform = `translate(0, 0) rotate(120deg)`;
  }
}

document.addEventListener('mousemove', animateButtonMove);

document.addEventListener('mouseleave', () => {
  button.style.transition = "transform 0.03s linear";
  button.style.transform = 'translate(moveRandomX, moveRandomY) rotate(0deg)';
});
