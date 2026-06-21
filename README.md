# BookTok & Female Wellness Viral Content Generator

A comprehensive Python-based system for generating, adapting, and publishing viral short-form content for BookTok and female wellness niches. Optimized for TikTok and Instagram Reels with seamless e-commerce product integration.

## Features

- **BookTok Content Analyzer**: Analyze viral book-related reels, identify trending tropes, spicy scenes, character moments
- **Wellness Content Adaptation**: Transform trending wellness content for your brand's voice
- **Smart Hook Generator**: Create scroll-stopping hooks based on viral BookTok patterns ("POV:", "IYKYK", "This book made me...", etc.)
- **Character & Plot Synthesis**: Generate content ideas around book characters, romance tropes, plot twists
- **Product Integration**: Seamlessly link your e-commerce products (journals, wellness guides, signed books, merchandise)
- **Multi-Platform Publishing**: Auto-post to TikTok and Instagram Reels with platform-specific formatting
- **Audio Sync**: Match trending sounds and music across platforms
- **Performance Analytics**: Track views, engagement, saves, and conversion to product sales
- **Trend Monitoring**: Real-time tracking of trending BookTok sounds, hashtags, and viral formats

## Niche Focus

- **BookTok**: Romance, dark academia, fantasy, contemporary, LGBTQ+, book recommendations, reading vlogs
- **Female Wellness**: Mental health, self-care, fitness, nutrition, productivity, manifestation, personal growth

## Project Structure

```
├── config/
│   ├── brand_config.json          # Your brand voice, product catalog
│   ├── platform_settings.json      # TikTok/Reels API credentials
│   ├── booktok_templates.json      # Viral BookTok format templates
│   ├── wellness_templates.json     # Viral wellness format templates
│   └── credentials.env             # API keys (git-ignored)
├── src/
│   ├── content_analyzer.py         # Analyze viral reels in niche
│   ├── content_generator.py        # Generate new content from patterns
│   ├── content_adapter.py          # Adapt viral content for your brand
│   ├── booktok_generator.py        # BookTok-specific generation logic
│   ├── wellness_generator.py       # Wellness-specific generation logic
│   ├── platform_publisher.py       # Publish to TikTok & Instagram
│   ├── trend_monitor.py            # Track trending sounds & hashtags
│   ├── product_integrator.py       # Link to e-commerce products
│   └── analytics.py                # Performance tracking & insights
├── data/
│   ├── viral_templates/
│   │   ├── booktok_hooks.json
│   │   ├── wellness_hooks.json
│   │   └── transition_styles.json
│   ├── products.json               # Your e-commerce product catalog
│   ├── books.json                  # Your book recommendations
│   └── trending_sounds.json        # Cached trending audio
├── scripts/
│   ├── main.py                     # Main content generation pipeline
│   ├── generate_booktok.py         # Generate BookTok content
│   ├── generate_wellness.py        # Generate wellness content
│   ├── schedule_posts.py           # Schedule publishing
│   ├── analyze_performance.py      # Analytics & insights
│   └── sync_trends.py              # Update trending content
├── tests/
│   └── test_generators.py
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/luisangellavander-afk/social-media-script.git
cd social-media-script
pip install -r requirements.txt
cp config/credentials.env.example config/credentials.env
# Edit credentials.env with your TikTok & Instagram API keys
```

## Quick Start

### Generate BookTok Content
```bash
python scripts/main.py --mode generate --niche booktok --count 5 --product-link
```

### Generate Wellness Content
```bash
python scripts/main.py --mode generate --niche wellness --count 5 --product-link
```

### Generate Both Niches
```bash
python scripts/main.py --mode generate --niche both --count 10 --save
```

### Check Trending Content
```bash
python scripts/main.py --mode trends --niche booktok
```

### Schedule Auto-Publishing
```bash
python scripts/schedule_posts.py \
  --platform tiktok,instagram \
  --time "09:00,14:00,20:00" \
  --optimal-posting True
```

### Analyze Performance
```bash
python scripts/analyze_performance.py \
  --days 7 \
  --output dashboard
```

## Configuration

### Brand Config (`config/brand_config.json`)
```json
{
  "brand": {
    "name": "Your Name",
    "tagline": "BookTok & Female Wellness Creator",
    "voice": "authentic, relatable, inspiring",
    "posting_schedule": {
      "tiktok": ["09:00", "14:00", "20:00", "22:00"],
      "instagram": ["10:00", "15:00", "19:00", "21:00"]
    }
  },
  "products": {
    "books": [...],
    "wellness_guides": [...],
    "merchandise": [...]
  }
}
```

## Content Generation Patterns

### BookTok Viral Hooks
- "POV: You just finished this book and can't stop thinking about..."
- "This book is currently IYKYK but let me tell you why..."
- "Hot take: This character is..."
- "The way this book made me feel..."
- "Book recommendation that'll change your life:"
- "Plot twist I didn't see coming:"

### Wellness Viral Hooks
- "My 30-day transformation to..."
- "I tried this wellness trend and here's what happened:"
- "This one habit changed my entire routine:"
- "POV: You're about to start your healing journey..."
- "Productivity hack nobody talks about:"

## API Requirements

- **TikTok API** (Business Account) - for posting & analytics
- **Instagram Graph API** - for Reels posting & analytics
- **OpenAI / Anthropic API** - for intelligent content generation
- **Optional: TikTok Research API** - for trend data

## Key Features Explained

### 1. Content Generator
Uses LLMs (GPT-4 or Claude) to create original content based on:
- Your brand voice and personality
- Viral hook templates and patterns
- Current trending sounds and hashtags
- Your product catalog

### 2. Platform Publisher
Handles multi-platform publishing:
- Video formatting for TikTok and Instagram Reels
- Optimal posting times based on your audience
- Caption optimization with hashtags
- Sound syncing
- Scheduled posting

### 3. Trend Monitor
Tracks what's viral in your niche:
- Top trending sounds (updated daily)
- Viral hashtags and growth rates
- Content format patterns
- Engagement metrics

### 4. Product Integration
Seamlessly link to your e-commerce:
- Direct product mentions in captions
- Affiliate links
- UTM parameter tracking
- Click-through rate monitoring

## Workflow

1. **Analyze** trending BookTok/wellness content daily
2. **Generate** 5-10 content ideas using AI patterns
3. **Adapt** ideas for your brand and products
4. **Create** video scripts and hooks
5. **Schedule** posts for optimal times
6. **Monitor** performance in real-time
7. **Iterate** based on analytics

## Monetization Strategies

- TikTok Creator Fund & Shop
- Instagram Reels Bonus Program
- Affiliate commissions (books, wellness products)
- Direct product sales through e-commerce
- Brand partnerships in niche

## Best Practices

✅ Post 3-5x weekly for algorithm growth  
✅ Post during peak hours (evening/weekend for female wellness audience)  
✅ Use trending sounds within 48 hours of trend start  
✅ Engage with comments in first hour (critical for algorithm)  
✅ Mix content types (POVs, reviews, hauls, recommendations, personal stories)  
✅ Cross-post to Instagram Reels for 2x reach  
✅ Track which hooks and formats drive product sales  

## Development

### Install Development Dependencies
```bash
pip install -r requirements.txt
pip install pytest pytest-cov black flake8
```

### Run Tests
```bash
pytest tests/
```

### Format Code
```bash
black src/ scripts/
```

## Contributing

Contributions are welcome! Please:
1. Create a feature branch (`git checkout -b feature/amazing-feature`)
2. Commit changes (`git commit -m 'Add amazing feature'`)
3. Push to branch (`git push origin feature/amazing-feature`)
4. Open a Pull Request

## License

MIT - Feel free to use, modify, and distribute

## Support

For issues, feature requests, or questions about content generation strategies, please open an issue on GitHub.

## Connect

- **GitHub**: [@luisangellavander-afk](https://github.com/luisangellavander-afk)
- **Twitter/X**: [@your_handle](https://twitter.com)
- **TikTok**: [@your_handle](https://tiktok.com)

---

**Made with ❤️ for BookTok creators and wellness enthusiasts**
