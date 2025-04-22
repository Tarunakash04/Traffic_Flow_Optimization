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

  
  function updateUI() {
    laneOrder.forEach((lane, i) => {
      const laneNum = i + 1;
      const isGreen = i === currentGreenIndex;
      const signalEl = document.getElementById(`signal${laneNum}`);
      const timerEl = document.getElementById(`timer${laneNum}`);
      const countEl = document.getElementById(`count${laneNum}`);
      const carsContainer = document.getElementById(`cars${laneNum}`);
  
      // Signal color
      signalEl.className = `signal ${isGreen ? 'green' : 'red'}`;
      timerEl.innerText = isGreen ? `Green for: ${greenTime}s` : `Red`;
  
      // Update vehicle count text
      countEl.innerText = `${lane}: 🚗 x ${trafficData[lane].count}`;
  
      // Animate cars on green
      carsContainer.innerHTML = '';
      if (isGreen) {
        for (let j = 0; j < Math.min(5, trafficData[lane].count); j++) {
          const car = document.createElement('div');
          car.className = 'car';
          car.innerText = '🚗';
          carsContainer.appendChild(car);
        }
      }
    });
  }
  
  setInterval(() => {
    greenTime--;
  
    laneOrder.forEach((lane, i) => {
      const isGreen = i === currentGreenIndex;
      const traffic = trafficData[lane];
  
      if (isGreen) {
        // 🧠 Realistic signal flow logic (based on phase)
        const phase = greenTimeOriginal - greenTime;
        let carsToPass = 1; // Default: slow phase
  
        if (phase <= 3) {
          carsToPass = 4; // Burst start 🚀
        } else if (phase <= 8) {
          carsToPass = 2; // Steady stream
        }
  
        traffic.count -= Math.min(traffic.count, carsToPass); // Prevent going negative
      } else {
        // 🔴 Red lanes build up
        traffic.count += 1;
      }
    });
  
    // 💡 Switch signal when green time ends
    if (greenTime <= 0) {
      currentGreenIndex = (currentGreenIndex + 1) % laneOrder.length;
  
      const nextLane = laneOrder[currentGreenIndex];
      const nextTraffic = trafficData[nextLane];
  
      // 🧮 Smart green time calc (based on vehicle pressure)
      greenTime = Math.min(30, Math.floor(nextTraffic.count / 2.3));
      greenTime = Math.max(greenTime, 5); // Minimum green duration
  
      greenTimeOriginal = greenTime; // Store original for phase tracking
    }
  
    updateUI();
  }, 200);
  