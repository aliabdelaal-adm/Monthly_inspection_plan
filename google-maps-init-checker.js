/**
 * Google Maps Initialization Checker
 * مُتحقق من تهيئة خرائط جوجل
 * 
 * This script ensures that GOOGLE_MAPS_CONFIG and googleMapsLoader are always available
 * يضمن هذا السكريبت أن GOOGLE_MAPS_CONFIG و googleMapsLoader متاحة دائماً
 * 
 * This should be loaded AFTER google-maps-config.js and google-maps-loader.js
 * يجب تحميل هذا الملف بعد google-maps-config.js و google-maps-loader.js
 * 
 * Version: 1.0
 * Last Updated: 2025-11-13
 */

(function() {
    'use strict';
    
    console.log('🔍 Checking Google Maps initialization...');
    console.log('🔍 فحص تهيئة خرائط جوجل...');
    
    // Check if GOOGLE_MAPS_CONFIG exists
    if (typeof window.GOOGLE_MAPS_CONFIG === 'undefined') {
        console.error('❌ GOOGLE_MAPS_CONFIG not found! Creating minimal config...');
        console.error('❌ GOOGLE_MAPS_CONFIG غير موجود! إنشاء إعداد أساسي...');
        
        // Create a minimal configuration
        window.GOOGLE_MAPS_CONFIG = {
            apiKey: window.GOOGLE_MAPS_API_KEY || 'YOUR_API_KEY_HERE',
            mapConfig: {
                defaultCenter: { lat: 24.4539, lng: 54.3773 },
                defaultZoom: 12,
                minZoom: 10,
                maxZoom: 18,
                styles: []
            },
            libraries: ['places', 'geocoding'],
            language: 'ar',
            region: 'AE',
            features: {
                enableAutoGeocoding: true,
                geocodingBatchSize: 10,
                geocodingDelay: 100,
                nearbyRadius: 2000,
                areaOverlapOffset: 0.005,
                markerColors: {
                    'very-high': '#8b0000',
                    'high': '#dc3545',
                    'medium': '#ffc107',
                    'normal': '#667eea',
                    'selected': '#28a745',
                    'unavailable': '#999999'
                }
            },
            loading: {
                maxRetryAttempts: 3,
                retryDelay: 2000,
                scriptTimeout: 15000
            },
            messages: {
                ar: {
                    loading: 'جاري تحميل خرائط جوجل...',
                    ready: 'خرائط جوجل جاهزة',
                    error: 'فشل تحميل الخرائط'
                },
                en: {
                    loading: 'Loading Google Maps...',
                    ready: 'Google Maps Ready',
                    error: 'Failed to load Google Maps'
                }
            }
        };
        
        console.log('✅ Created fallback GOOGLE_MAPS_CONFIG');
        console.log('✅ تم إنشاء GOOGLE_MAPS_CONFIG احتياطي');
    } else {
        console.log('✅ GOOGLE_MAPS_CONFIG is loaded');
        console.log('✅ GOOGLE_MAPS_CONFIG محمّل');
    }
    
    // Check if googleMapsLoader exists
    if (typeof window.googleMapsLoader === 'undefined') {
        console.error('❌ googleMapsLoader not found! Attempting to create...');
        console.error('❌ googleMapsLoader غير موجود! محاولة الإنشاء...');
        
        // Check if GoogleMapsLoader class is available
        if (typeof GoogleMapsLoader !== 'undefined') {
            window.googleMapsLoader = new GoogleMapsLoader(window.GOOGLE_MAPS_CONFIG);
            console.log('✅ Created googleMapsLoader from class');
            console.log('✅ تم إنشاء googleMapsLoader من الفئة');
        } else {
            console.error('❌ GoogleMapsLoader class not available! google-maps-loader.js may not have loaded.');
            console.error('❌ فئة GoogleMapsLoader غير متاحة! قد لا يكون google-maps-loader.js قد تم تحميله.');
            console.error('⚠️ Google Maps functionality will be limited.');
            console.error('⚠️ وظائف خرائط جوجل ستكون محدودة.');
            
            // Create a minimal stub to prevent errors
            window.googleMapsLoader = {
                isLoaded: false,
                isLoading: false,
                loadAttempts: 0,
                getStatus: function() { return 'error'; },
                init: function() {
                    return Promise.reject(new Error('GoogleMapsLoader class not available'));
                },
                on: function() {}
            };
            
            console.log('⚠️ Created minimal googleMapsLoader stub');
            console.log('⚠️ تم إنشاء نسخة أساسية من googleMapsLoader');
        }
    } else {
        console.log('✅ googleMapsLoader is loaded');
        console.log('✅ googleMapsLoader محمّل');
    }
    
    // Final validation
    const configLoaded = typeof window.GOOGLE_MAPS_CONFIG !== 'undefined';
    const loaderLoaded = typeof window.googleMapsLoader !== 'undefined';
    
    if (configLoaded && loaderLoaded) {
        console.log('✅✅ All Google Maps components initialized successfully!');
        console.log('✅✅ تم تهيئة جميع مكونات خرائط جوجل بنجاح!');
    } else {
        console.error('❌ Some Google Maps components failed to initialize:');
        console.error(`   - GOOGLE_MAPS_CONFIG: ${configLoaded ? '✅' : '❌'}`);
        console.error(`   - googleMapsLoader: ${loaderLoaded ? '✅' : '❌'}`);
    }
})();
