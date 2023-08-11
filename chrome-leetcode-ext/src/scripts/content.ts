// Copyright 2022 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
const values = new Map();
const axios = require('axios');
const LAMBDA_URL = ''

let submitButton
let problemDescription
let elementsWithClass
let difficulty
let problemTitle
let currentUrl
let formattedTitle
let descriptionFormatted

const handleButtonClick = () => {
  const codeEditorElement = document.querySelector('[data-track-load="code_editor"]');
  if (codeEditorElement) {
    const linesContentElement = codeEditorElement!.querySelector('.lines-content') as HTMLElement;
    values.set("submit", linesContentElement.innerText)

    setTimeout(() => {
      const submissionResult = document.querySelector('[data-e2e-locator="submission-result"]') as HTMLElement;
      if (submissionResult.innerText === "Accepted") {
        const req = {
          "title": values.get('title'),
          "code_answer": linesContentElement.innerText,
          "readme": values.get('readme'),
          "difficulty": values.get('difficulty'),
        }
        try {
          axios.post(LAMBDA_URL, req)
        } catch (e) {
          console.log(e)
        }
      }

    }, 5000)
  }
}

setTimeout(() => {
  submitButton = document.querySelector('[data-e2e-locator="console-submit-button"]') as HTMLElement;
  problemDescription = document.querySelector('[data-track-load="description_content"]') as HTMLElement;
  elementsWithClass = document.querySelectorAll('div.flex.space-x-4');
  difficulty = document.querySelector('.text-yellow, .text-pink, .text-olive') as HTMLElement;

  if (!elementsWithClass || !problemDescription) return
  problemTitle = elementsWithClass[1] as HTMLElement;
  currentUrl = window.location.href;
  formattedTitle = problemTitle.innerText.replace(/\./g, "").replace(/ /g, "-");

  descriptionFormatted = problemDescription.innerHTML.replace(/<p>&nbsp;<\/p>/g, "")
  values.set( 'difficulty', difficulty.innerText)
  values.set( 'title', formattedTitle)
  values.set('readme', '## [' + problemTitle.innerText + '](' + currentUrl + ')\n' + '## ' + difficulty.innerText + '\n' + descriptionFormatted)
  
  if (submitButton) {
    submitButton.addEventListener('click', handleButtonClick)
  }
}, 2000)

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {

    if (request.message === 'hello!') {
      console.log(request.url)
    }

    setTimeout(() => {
      submitButton = document.querySelector('[data-e2e-locator="console-submit-button"]') as HTMLElement;
      problemDescription = document.querySelector('[data-track-load="description_content"]') as HTMLElement;
      elementsWithClass = document.querySelectorAll('div.flex.space-x-4');
      difficulty = document.querySelector('.text-yellow, .text-pink, .text-olive') as HTMLElement;

      if (!elementsWithClass || !problemDescription) return
      problemTitle = elementsWithClass[1] as HTMLElement;
      currentUrl = window.location.href;
      formattedTitle = problemTitle?.innerText?.replace(/\./g, "")?.replace(/ /g, "-");
    
      descriptionFormatted = problemDescription.innerHTML.replace(/<p>&nbsp;<\/p>/g, "")
      values.set( 'difficulty', difficulty.innerText)
      values.set( 'title', formattedTitle)
      values.set('readme', '## [' + problemTitle.innerText + '](' + currentUrl + ')\n' + '## ' + difficulty.innerText + '\n' + descriptionFormatted)

      if (submitButton) {
        submitButton.addEventListener('click', handleButtonClick)
      }
    }, 2000)

});
