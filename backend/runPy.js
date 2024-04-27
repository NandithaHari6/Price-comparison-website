const { spawn } = require('child_process');

function runPythonScript(scriptPath, args) {
    return new Promise((resolve, reject) => {
        const pythonProcess = spawn('python', [scriptPath, ...args]);

        let output = '';
        let errorOutput = '';


        pythonProcess.stderr.on('data', (data) => {
            errorOutput += data.toString();
        });
        
        pythonProcess.on('close', (code) => {
            if (code === 0) {
                resolve(output);
            } else {
                reject(errorOutput || `Python script exited with code ${code}`);
            }
        });
    });
}

// Usage
const scriptPath = '..\\webscraper.py';
const args = ['oppo', 'phone']; // Array of command-line arguments

runPythonScript(scriptPath, args)
    .then((output) => {
        console.log(`Python script output: ${output}`);
    })
    .catch((error) => {
        console.error(`Error: ${error}`);
    });