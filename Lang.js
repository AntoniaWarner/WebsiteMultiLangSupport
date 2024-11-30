window.addEventListener('DOMContentLoaded', async () => {
    const userPreferredLanguage = localStorage.getItem('language') || 'nl';
    const langData = await fetchLanguageData(userPreferredLanguage);
    updateContent(langData);
    console.log("Event Heard");
    
});
function updateContent(langData) {
    document.querySelectorAll('[data-key]').forEach(element => {
        const key = element.getAttribute('data-key');
        element.textContent = langData[key];
        
    });
    console.log("Content Updated");
}
function setLanguagePreference(lang) {
    localStorage.setItem('language', lang);
    location.reload();
    console.log("Language Set");
}
async function fetchLanguageData(lang) {
    const response = await fetch(`../Languages/${lang}.json`);
    console.log("Data Fetched");
    return response.json();
}
async function changeLanguage(lang) {
    await setLanguagePreference(lang);
    
    const langData = await fetchLanguageData(lang);
    console.log("Lang Changed");
    updateContent(langData);
}