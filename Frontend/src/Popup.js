import React from 'react';

function Popup({ handleClose, children }) {
  return (
    <div className="popup">
      <div className="popup-inner">
        
        {children}
      </div>
    </div>
  );
}

export default Popup;