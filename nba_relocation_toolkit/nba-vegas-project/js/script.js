// Load the CSV data
Papa.parse("data/fans_surv_responses.csv", {
  download: true,
  header: true,
  complete: function(results) {
    console.log("Parsed Data:", results.data);

    // Placeholder: we'll visualize this next
    document.getElementById("chart-container").innerText = 
      `Loaded ${results.data.length} responses. Check console for full data.`;
  }
});
