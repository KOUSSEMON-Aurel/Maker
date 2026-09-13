import { ThemeName } from '../types';

export interface ThemeConfig {
  name: string;
  bgGradient: string;
  accentColor: string;
  secondaryColor: string;
  textColor: string;
  cardBg: string;
  cardBorder: string;
  fontFamily: string;
  shadow: string;
}

export const THEMES: Record<ThemeName, ThemeConfig> = {
  dark_tech: {
    name: 'Dark Tech',
    bgGradient: 'radial-gradient(circle at 50% 30%, #111827 0%, #030712 100%)',
    accentColor: '#00F5FF',      // Neon cyan
    secondaryColor: '#10B981',   // Neon green
    textColor: '#F9FAFB',
    cardBg: 'rgba(17, 24, 39, 0.85)',
    cardBorder: 'rgba(0, 245, 255, 0.3)',
    fontFamily: '"Space Grotesk", "Clash Display", sans-serif',
    shadow: '0 20px 40px rgba(0, 245, 255, 0.15)',
  },
  punchy_creator: {
    name: 'Punchy Creator',
    bgGradient: 'radial-gradient(circle at 50% 20%, #1F1F2E 0%, #0D0D12 100%)',
    accentColor: '#FFDD00',      // Electric yellow
    secondaryColor: '#A855F7',   // Vibrant purple
    textColor: '#FFFFFF',
    cardBg: 'rgba(28, 28, 40, 0.88)',
    cardBorder: 'rgba(255, 221, 0, 0.35)',
    fontFamily: '"Montserrat", "Inter", sans-serif',
    shadow: '0 20px 50px rgba(0, 0, 0, 0.6)',
  },
  minimalist_swiss: {
    name: 'Minimalist Swiss',
    bgGradient: 'radial-gradient(circle at 50% 50%, #18181B 0%, #09090B 100%)',
    accentColor: '#EF4444',      // Swiss red
    secondaryColor: '#E4E4E7',
    textColor: '#FAFAFA',
    cardBg: 'rgba(24, 24, 27, 0.92)',
    cardBorder: 'rgba(255, 255, 255, 0.12)',
    fontFamily: '"Cabinet Grotesk", "Satoshi", sans-serif',
    shadow: '0 25px 50px rgba(0, 0, 0, 0.7)',
  },
  vintage_archive: {
    name: 'Vintage Archive',
    bgGradient: 'radial-gradient(circle at 50% 40%, #291F18 0%, #120D0A 100%)',
    accentColor: '#F59E0B',      // Aged amber/gold
    secondaryColor: '#D97706',
    textColor: '#F5F5F4',
    cardBg: 'rgba(38, 28, 22, 0.9)',
    cardBorder: 'rgba(245, 158, 11, 0.3)',
    fontFamily: '"Playfair Display", Georgia, serif',
    shadow: '0 20px 45px rgba(0, 0, 0, 0.8)',
  },
};
