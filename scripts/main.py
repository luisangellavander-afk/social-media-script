#!/usr/bin/env python3
"""
Main entry point for viral social media content generation.
Generates BookTok and wellness content optimized for TikTok and Instagram Reels.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from content_generator import ContentGenerator
from trend_monitor import TrendMonitor


def main():
    parser = argparse.ArgumentParser(
        description="Viral Social Media Content Generator for BookTok & Female Wellness"
    )

    parser.add_argument(
        "--mode",
        choices=["generate", "trends", "publish"],
        default="generate",
        help="Mode of operation"
    )

    parser.add_argument(
        "--niche",
        choices=["booktok", "wellness", "both"],
        default="both",
        help="Content niche"
    )

    parser.add_argument(
        "--count",
        type=int,
        default=5,
        help="Number of content ideas to generate"
    )

    parser.add_argument(
        "--product-link",
        action="store_true",
        help="Include product links in content"
    )

    parser.add_argument(
        "--save",
        action="store_true",
        default=True,
        help="Save generated content to file"
    )

    args = parser.parse_args()

    # Initialize components
    generator = ContentGenerator()
    trend_monitor = TrendMonitor()

    print(f"🚀 BookTok & Wellness Content Generator")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Mode: Generate content
    if args.mode == "generate":
        print(f"📝 Generating {args.niche} content...\n")

        results = {}

        if args.niche in ["booktok", "both"]:
            print("🎬 BookTok Content:")
            booktok_ideas = generator.generate_booktok_content(
                count=args.count,
                product_link=args.product_link
            )
            results["booktok"] = booktok_ideas

            for i, idea in enumerate(booktok_ideas, 1):
                print(f"\n  {i}. {idea['hook_category'].replace('_', ' ').title()}")
                print(f"     Hashtags: {' '.join(idea['hashtags'][:5])}")

        if args.niche in ["wellness", "both"]:
            print("\n💪 Wellness Content:")
            wellness_ideas = generator.generate_wellness_content(
                count=args.count,
                product_link=args.product_link
            )
            results["wellness"] = wellness_ideas

            for i, idea in enumerate(wellness_ideas, 1):
                print(f"\n  {i}. {idea['hook_category'].replace('_', ' ').title()}")
                print(f"     Hashtags: {' '.join(idea['hashtags'][:5])}")

        # Save results
        if args.save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"data/generated_content_{timestamp}.json"
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            print(f"\n✅ Content saved to {output_file}")

    # Mode: Trends
    elif args.mode == "trends":
        print(f"📊 Checking trending content in {args.niche}...\n")
        
        if args.niche in ["booktok", "both"]:
            insights = trend_monitor.get_niche_insights("booktok")
            print("🎬 BookTok Trends:")
            print("\n🎵 Trending Sounds:")
            for sound in insights["trending_sounds"][:5]:
                print(f"  {sound['name']} - {sound['uses']:,} uses {sound['growth']}")
            
            print("\n📊 Trending Hashtags:")
            for tag in insights["trending_hashtags"][:5]:
                print(f"  {tag['tag']} - {tag['uses']:,} uses {tag['growth']}")
        
        if args.niche in ["wellness", "both"]:
            insights = trend_monitor.get_niche_insights("wellness")
            print("\n💪 Wellness Trends:")
            print("\n🎵 Trending Sounds:")
            for sound in insights["trending_sounds"][:5]:
                print(f"  {sound['name']} - {sound['uses']:,} uses {sound['growth']}")
            
            print("\n📊 Trending Hashtags:")
            for tag in insights["trending_hashtags"][:5]:
                print(f"  {tag['tag']} - {tag['uses']:,} uses {tag['growth']}")

    print("\n" + "="*60)
    print("💡 Next Steps:")
    if args.mode == "generate":
        print("   1. Review generated content ideas")
        print("   2. Create video scripts")
        print("   3. Record and edit videos")
        print("   4. Use API credentials to auto-publish")
    print("="*60)


if __name__ == "__main__":
    main()
