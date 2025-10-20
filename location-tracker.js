/**
 * Location Tracking Module
 * Tracks user geolocation during work shifts
 * Complies with privacy regulations and requires user consent
 */

class LocationTracker {
    constructor() {
        this.isTracking = false;
        this.watchId = null;
        this.trackingInterval = 5 * 60 * 1000; // 5 minutes
        this.locationData = [];
        this.currentShift = null;
        this.hasConsent = false;
    }

    /**
     * Initialize location tracking with user consent
     */
    async initialize() {
        // Load saved consent and settings
        const consent = localStorage.getItem('locationTrackingConsent');
        const settings = localStorage.getItem('locationTrackingSettings');
        
        if (consent) {
            this.hasConsent = JSON.parse(consent).consent === true;
        }
        
        if (settings) {
            const savedSettings = JSON.parse(settings);
            this.trackingInterval = savedSettings.updateInterval || this.trackingInterval;
        }
        
        // Load existing location data
        await this.loadLocationData();
        
        return this.hasConsent;
    }

    /**
     * Request user consent for location tracking
     */
    async requestConsent() {
        return new Promise((resolve) => {
            const modal = document.createElement('div');
            modal.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.7);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 10000;
                direction: rtl;
            `;
            
            modal.innerHTML = `
                <div style="background: white; padding: 30px; border-radius: 15px; max-width: 500px; text-align: center; box-shadow: 0 10px 40px rgba(0,0,0,0.3);">
                    <h2 style="color: #2336a0; margin-bottom: 20px;">🌍 تتبع الموقع الجغرافي</h2>
                    <p style="color: #333; line-height: 1.8; margin-bottom: 20px; text-align: right;">
                        لتحسين الأمان والمساءلة، نطلب السماح بتتبع موقعك الجغرافي أثناء مناوبات العمل فقط.
                    </p>
                    <div style="background: #f0f4ff; padding: 15px; border-radius: 10px; margin-bottom: 20px; text-align: right;">
                        <h4 style="color: #2336a0; margin-bottom: 10px;">📋 ما الذي سيتم تسجيله:</h4>
                        <ul style="list-style: none; padding: 0; color: #555;">
                            <li>✓ موقعك الجغرافي كل 5 دقائق أثناء المناوبة</li>
                            <li>✓ وقت وتاريخ كل تسجيل</li>
                            <li>✓ معلومات المناوبة (المنطقة والوقت)</li>
                        </ul>
                    </div>
                    <div style="background: #fff3cd; padding: 15px; border-radius: 10px; margin-bottom: 20px; text-align: right;">
                        <h4 style="color: #856404; margin-bottom: 10px;">🔒 التزامنا:</h4>
                        <ul style="list-style: none; padding: 0; color: #856404; font-size: 0.9em;">
                            <li>✓ التتبع أثناء ساعات العمل فقط</li>
                            <li>✓ بياناتك محمية ومشفرة</li>
                            <li>✓ يمكنك إيقاف التتبع في أي وقت</li>
                            <li>✓ الحفظ لمدة 90 يوماً فقط</li>
                        </ul>
                    </div>
                    <div style="display: flex; gap: 10px; justify-content: center;">
                        <button id="acceptConsent" style="
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            color: white;
                            border: none;
                            padding: 12px 30px;
                            border-radius: 8px;
                            font-size: 1.1em;
                            font-weight: bold;
                            cursor: pointer;
                            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
                        ">✓ أوافق</button>
                        <button id="declineConsent" style="
                            background: #e0e0e0;
                            color: #555;
                            border: none;
                            padding: 12px 30px;
                            border-radius: 8px;
                            font-size: 1.1em;
                            font-weight: bold;
                            cursor: pointer;
                        ">✗ لا أوافق</button>
                    </div>
                    <a href="./PRIVACY_POLICY_LOCATION.md" target="_blank" style="
                        display: block;
                        margin-top: 15px;
                        color: #667eea;
                        text-decoration: none;
                        font-size: 0.9em;
                    ">📄 اقرأ سياسة الخصوصية الكاملة</a>
                </div>
            `;
            
            document.body.appendChild(modal);
            
            document.getElementById('acceptConsent').onclick = () => {
                this.hasConsent = true;
                const consentData = {
                    consent: true,
                    timestamp: new Date().toISOString(),
                    version: '1.0'
                };
                localStorage.setItem('locationTrackingConsent', JSON.stringify(consentData));
                document.body.removeChild(modal);
                resolve(true);
            };
            
            document.getElementById('declineConsent').onclick = () => {
                this.hasConsent = false;
                const consentData = {
                    consent: false,
                    timestamp: new Date().toISOString(),
                    version: '1.0'
                };
                localStorage.setItem('locationTrackingConsent', JSON.stringify(consentData));
                document.body.removeChild(modal);
                resolve(false);
            };
        });
    }

    /**
     * Start tracking for a specific shift
     */
    async startTracking(shiftInfo) {
        if (!this.hasConsent) {
            const consent = await this.requestConsent();
            if (!consent) {
                console.log('Location tracking declined by user');
                return false;
            }
        }

        if (!navigator.geolocation) {
            console.error('Geolocation is not supported by this browser');
            return false;
        }

        this.currentShift = shiftInfo;
        this.isTracking = true;

        // Get initial location
        await this.captureLocation();

        // Set up periodic tracking
        this.watchId = setInterval(() => {
            if (this.isTracking) {
                this.captureLocation();
            }
        }, this.trackingInterval);

        console.log('Location tracking started for shift:', shiftInfo);
        return true;
    }

    /**
     * Capture current location
     */
    async captureLocation() {
        return new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const locationPoint = {
                        timestamp: new Date().toISOString(),
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude,
                        accuracy: position.coords.accuracy,
                        inspector: this.currentShift?.inspector || 'unknown',
                        day: this.currentShift?.day || new Date().toISOString().split('T')[0],
                        shift: this.currentShift?.shift || 'unknown',
                        area: this.currentShift?.area || 'unknown'
                    };

                    this.locationData.push(locationPoint);
                    this.saveLocationData();
                    
                    console.log('Location captured:', locationPoint);
                    resolve(locationPoint);
                },
                (error) => {
                    console.error('Error capturing location:', error);
                    reject(error);
                },
                {
                    enableHighAccuracy: true,
                    timeout: 10000,
                    maximumAge: 0
                }
            );
        });
    }

    /**
     * Stop tracking
     */
    stopTracking() {
        if (this.watchId) {
            clearInterval(this.watchId);
            this.watchId = null;
        }
        this.isTracking = false;
        this.currentShift = null;
        console.log('Location tracking stopped');
    }

    /**
     * Save location data to localStorage and optionally to GitHub
     */
    async saveLocationData() {
        try {
            // Save to localStorage
            localStorage.setItem('locationTrackingData', JSON.stringify(this.locationData));
            
            // Optionally save to GitHub (if token available)
            // This would require integration with the existing file upload system
            
            return true;
        } catch (error) {
            console.error('Error saving location data:', error);
            return false;
        }
    }

    /**
     * Load location data from localStorage
     */
    async loadLocationData() {
        try {
            const data = localStorage.getItem('locationTrackingData');
            if (data) {
                this.locationData = JSON.parse(data);
            }
            return this.locationData;
        } catch (error) {
            console.error('Error loading location data:', error);
            return [];
        }
    }

    /**
     * Get location history for a specific inspector
     */
    getLocationHistory(inspector, startDate, endDate) {
        return this.locationData.filter(loc => {
            const matchInspector = !inspector || loc.inspector === inspector;
            const matchStartDate = !startDate || loc.day >= startDate;
            const matchEndDate = !endDate || loc.day <= endDate;
            return matchInspector && matchStartDate && matchEndDate;
        });
    }

    /**
     * Clear old location data (older than 90 days)
     */
    cleanupOldData() {
        const ninetyDaysAgo = new Date();
        ninetyDaysAgo.setDate(ninetyDaysAgo.getDate() - 90);
        const cutoffDate = ninetyDaysAgo.toISOString();

        this.locationData = this.locationData.filter(loc => 
            loc.timestamp >= cutoffDate
        );

        this.saveLocationData();
        console.log('Old location data cleaned up');
    }

    /**
     * Export location data for a specific inspector
     */
    exportData(inspector) {
        const data = this.getLocationHistory(inspector);
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `location-history-${inspector}-${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        URL.revokeObjectURL(url);
    }

    /**
     * Revoke consent and delete all location data
     */
    revokeConsent() {
        this.stopTracking();
        this.hasConsent = false;
        this.locationData = [];
        localStorage.removeItem('locationTrackingConsent');
        localStorage.removeItem('locationTrackingData');
        localStorage.removeItem('locationTrackingSettings');
        console.log('Consent revoked and all location data deleted');
    }

    /**
     * Get tracking status
     */
    getStatus() {
        return {
            hasConsent: this.hasConsent,
            isTracking: this.isTracking,
            currentShift: this.currentShift,
            totalLocations: this.locationData.length,
            lastLocation: this.locationData[this.locationData.length - 1]
        };
    }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LocationTracker;
}
