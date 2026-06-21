import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OutputRootTests(unittest.TestCase):
    def test_youtube_helpers_reject_empty_and_relative_outdir(self):
        scripts = [
            ROOT / "skills/xiaohu-video-md/scripts/youtube_audio_download.py",
            ROOT / "skills/xiaohu-video-md/scripts/youtube_subs_download.py",
            ROOT / "skills/xiaohu-video-download/scripts/youtube_download.py",
        ]
        for script in scripts:
            module = load_module(script)
            with self.subTest(script=script.name):
                with self.assertRaises(SystemExit):
                    module._load_output_root("")
                with self.assertRaises(SystemExit):
                    module._load_output_root("relative-output")

    def test_youtube_helpers_accept_absolute_outdir(self):
        script = ROOT / "skills/xiaohu-video-md/scripts/youtube_audio_download.py"
        module = load_module(script)
        with tempfile.TemporaryDirectory() as tmp:
            root = module._load_output_root(tmp)
            self.assertEqual(root, Path(tmp).resolve())
            self.assertTrue((root / "tmp").is_dir())
            self.assertTrue((root / "data").is_dir())


class BilingualAssTests(unittest.TestCase):
    def test_bilingual_srt_to_ass_keeps_size_contrast(self):
        module = load_module(ROOT / "skills/xiaohu-subtitle-polish/scripts/bilingual_ass.py")
        items = module.parse_srt(
            "1\n"
            "00:00:00,000 --> 00:00:02,000\n"
            "你好\n"
            "Hello\n"
        )
        ass = module.build_ass(items, cn_size=20, en_size=12)
        self.assertIn("Dialogue:", ass)
        self.assertIn("你好\\N{\\fs12}Hello", ass)


if __name__ == "__main__":
    unittest.main()
