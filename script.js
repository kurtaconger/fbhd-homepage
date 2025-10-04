// Modal functionality
function openModal(imageSrc, imageAlt) {
  const modal = document.getElementById('imageModal');
  const modalImage = document.getElementById('modalImage');
  
  modalImage.src = imageSrc;
  modalImage.alt = imageAlt;
  modal.style.display = 'grid';
  
  // Prevent body scroll when modal is open
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  const modal = document.getElementById('imageModal');
  modal.style.display = 'none';
  
  // Restore body scroll
  document.body.style.overflow = 'auto';
}

// Close modal on backdrop click
function handleBackdropClick(event) {
  if (event.target.classList.contains('modal-overlay')) {
    closeModal();
  }
}

// Close modal on Escape key
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeModal();
  }
});