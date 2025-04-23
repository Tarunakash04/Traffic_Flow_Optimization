const trafficData = {
  "Lane_1": { count: 3 },
  "Lane_2": { count: 3 },
  "Lane_3": { count: 3 },
  "Lane_4": { count: 3 }
};

let laneOrder = ["Lane_1", "Lane_2", "Lane_3", "Lane_4"];
let currentGreenIndex = 0;
let greenTime = 20;
let greenTimeOriginal = 0;
let festivalMode = false;
let emergencyLane = null;
let emergencyTimer = 0;
const emergencyDuration = 15; // seconds
const intervalSpeed = 200; // Interval speed set to 200ms

function updateUI() {
  laneOrder.forEach((lane, i) => {
      const laneNum = i + 1;
      const isGreen = (emergencyLane && emergencyLane === lane) || (!emergencyLane && i === currentGreenIndex);
      const signalEl = document.getElementById(`signal${laneNum}`);
      const timerEl = document.getElementById(`timer${laneNum}`);
      const countEl = document.getElementById(`count${laneNum}`);
      const carsContainer = document.getElementById(`cars${laneNum}`);

      // Signal color
      signalEl.className = `signal ${isGreen ? 'green' : 'red'}`;
      timerEl.innerText = isGreen ? `Green` : `Red`;
      if (isGreen && emergencyLane) {
          timerEl.innerText = `Emergency: ${emergencyTimer.toFixed(1)}s`;
      } else if (isGreen) {
          timerEl.innerText = `Green for: ${greenTime.toFixed(1)}s`;
      }

      // Update vehicle count text (ensuring whole number)
      countEl.innerText = `${lane}: 🚗 x ${Math.floor(trafficData[lane].count)}`;

      // Animate cars on green
      carsContainer.innerHTML = '';
      if (isGreen) {
          for (let j = 0; j < Math.min(5, Math.floor(trafficData[lane].count)); j++) {
              const car = document.createElement('div');
              car.className = 'car';
              car.innerText = '🚗';
              carsContainer.appendChild(car);
          }
      }
  });
}

setInterval(() => {
  if (!emergencyLane) {
      greenTime -= (intervalSpeed / 1000) * 1;
  } else if (emergencyTimer > 0) {
      emergencyTimer -= (intervalSpeed / 1000);
      if (emergencyLane && trafficData[emergencyLane].count > 0) {
          trafficData[emergencyLane].count -= (intervalSpeed / 1000) * 2; // Gradual decrease
          if (trafficData[emergencyLane].count < 0) {
              trafficData[emergencyLane].count = 0;
          }
      }
  } else if (emergencyLane && emergencyTimer <= 0) {
      emergencyLane = null; // Turn off emergency mode after timer expires
  }

  laneOrder.forEach((lane, i) => {
      const isGreen = (emergencyLane && emergencyLane === lane) || (!emergencyLane && i === currentGreenIndex);
      const traffic = trafficData[lane];

      if (isGreen && !emergencyLane) {
          const phase = greenTimeOriginal - greenTime;
          let carsToPass = 1;

          if (phase <= (intervalSpeed / 1000) * 1.5) {
              carsToPass = 4;
          } else if (phase <= (intervalSpeed / 1000) * 4) {
              carsToPass = 2;
          }

          traffic.count -= Math.min(traffic.count, carsToPass);
      } else if (!isGreen) {
          traffic.count += (intervalSpeed / 1000) * 0.5;
      }
  });

  if (greenTime <= 0 && !emergencyLane) {
      currentGreenIndex = (currentGreenIndex + 1) % laneOrder.length;
      const nextLane = laneOrder[currentGreenIndex];
      const nextTraffic = trafficData[nextLane];
      greenTime = Math.min(30, Math.floor(nextTraffic.count / 2.3));
      greenTime = Math.max(greenTime, 5);
      if (festivalMode) {
          greenTime = Math.min(60, Math.floor(nextTraffic.count / 1.8));
          greenTime = Math.max(greenTime, 10);
      }
      greenTimeOriginal = greenTime;
  }

  updateUI();
}, intervalSpeed);

function toggleFestival() {
  fetch('/toggle_festival', { method: 'POST' })
      .then(response => response.json())
      .then(data => {
          festivalMode = data.festival_mode;
          console.log('Festival Mode:', festivalMode);
      })
      .catch(error => console.error('Error toggling festival mode:', error));
}

function triggerEmergency() {
  const selectedLane = prompt("Enter lane for emergency (Lane_1, Lane_2, Lane_3, Lane_4) or 'off' to disable:");
  if (selectedLane) {
      fetch('/set_emergency_lane', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ lane: selectedLane }),
      })
      .then(response => response.json())
      .then(data => {
          emergencyLane = data.emergency_lane;
          if (emergencyLane) {
              emergencyTimer = emergencyDuration; // Start the emergency timer
          } else {
              emergencyTimer = 0;
          }
          console.log('Emergency Lane:', emergencyLane, 'Emergency Timer:', emergencyTimer);
      })
      .catch(error => console.error('Error setting emergency lane:', error));
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const festivalBtn = document.getElementById('festivalBtn');
  const emergencyBtn = document.getElementById('emergencyBtn');

  if (festivalBtn) {
      festivalBtn.addEventListener('click', toggleFestival);
  }

  if (emergencyBtn) {
      emergencyBtn.addEventListener('click', triggerEmergency);
  }
});