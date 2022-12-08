class Strings:
    START_MESSAGE = ("Hello there,\n"
                     "You can use me to create custom stickers packs using existing stickers or PNG files.\n"
                     "\n"
                     "Main commands:\n"
                     "/create to create a new pack\n"
                     "/add to add stickers to an existing pack\n"
                     "/help for more commands\n")

    HELP_MESSAGE = ("<b>Daftar perintah lengkap</b>:\n"
                    "- /create: buat paket baru (paket animasi didukung)\n"
                    "- /add: tambahkan stiker ke paket\n"
                    "- /remove: hapus stiker dari paket\n"
                    "- kirimkan saya stiker dan saya akan mengirimkan png-nya kembali\n"
                    "- /list: daftar paket Anda (maks 100 entri)\n"
                    "- /export: ekspor paket stiker sebagai zip file png\n"
                    "- /forgetme: hapus diri Anda dari basis data saya. Paket yang Anda buat <b>tidak</b> akan dihapus dari Telegram\n"
                    "- /readd <code>paket link</code>: menyimpan paket yang dibuat melalui bot, tetapi karena beberapa alasan tidak muncul dalam daftar Anda\n"
                    "- /cleanup: hapus dari daftar paket Anda semua paket yang telah Anda hapus menggunakan @stickers\n"
                    "- /tofile: konversi stiker dan emoji khusus ke file\n"
                    "- /toemoji: mengubah ukuran stiker statis sehingga dapat ditambahkan ke paket emoji khusus\n"
                    "\n"
                    "<b>Operasi lainnya</b>\n"
                    "Anda dapat menghapus paket, mengubah emoji stiker, mengubah urutan stiker, dan melihat statistik stiker / paket dari @stickers\n"
                    "\n"
                    "<b>Tips</b>:\n"
                    "- Saat menambahkan stiker, Anda dapat mengatur emojinya dengan mengirimkannya sebelum mengirim stiker\n"
                    "- Saat menambahkan stiker atau membuat paket, Anda dapat meneruskan stiker atau file PNG\n"
                    "- Saat menambahkan stiker sebagai PNG, Anda dapat meneruskan emojinya di keterangan\n"
                    "- /tofile mendukung emoji bendera <code>-png</code>: itu akan membuat bot mengirim stiker statis/emojis "
                    "sebagai png alih-alih webp\n"
                    "- /toemoji mendukung bendera berikut: <code>-c</code> (akan memotong ruang transparan "
                    "pada batas gambar) dan <code>-r</code> (tidak akan mempertahankan rasio aspek gambar jika "
                    "itu tidak persegi)\n"
                    "\n"
                    "<b>Info lainnya</b>\n"
                    "Semua paket yang Anda buat dengan saya memiliki tautan yang diakhiri oleh \"_by_{}\". Ini tidak dibuat dengan sengaja, "
                    "tapi sesuatu yang dipaksakan oleh Telegram\n"
                    "\n"
                    "<b>Cara yang benar untuk membangun paket kustom Anda sendiri</b>\n"
                    "Gunakan @MyPackBot. Itu tidak mencuri stiker seperti saya. Ini juga sangat cepat. Benar-benar disarankan")

    PACK_CREATION_WAITING_TITLE = ("Baiklah, paket stiker baru! Pilih jenis paket dengan tombol di bawah ini "
                                   "dan <b>kirimkan saya judul paket</b> (tidak boleh melebihi 64 karakter).\n\n"
                                   "Gunakan /cancel untuk membatalkan")

    PACK_CREATION_ANIMATED_WAITING_TITLE = ("Baiklah, paket animasi baru! Tolong kirimkan saya judul paket "
                                            "(tidak boleh melebihi 64 karakter).\n"
                                            "Gunakan /cancel untuk membatalkan")

    PACK_TITLE_TOO_LONG = "Maaf, judulnya harus max 64 karakter. Coba dengan judul lain"

    PACK_TITLE_CONTAINS_NEWLINES = "Maaf, judulnya harus satu baris (tidak ada karakter baris baru)"

    PACK_TITLE_INVALID_MESSAGE = ("Oh tidak! Ini bukan yang saya tunggu! Tolong kirimkan saya "
                                  "judul paket, atau /cancel")

    PACK_CREATION_WAITING_NAME = ("Bagus, ini akan menjadi judul paket: <i>{}</i>\n"
                                  "\n"
                                  "Tolong kirimkan saya apa yang akan menjadi tautan paket (harus maksimal {} karakter. "
                                  "<b>Tidak</b> perlu menyertakan <code>https://t.me/addstickers/</code>)")

    PACK_NAME_TOO_LONG = "Maaf, tautan ini terlalu panjang ({}/{}). Coba lagi dengan tautan lain"

    PACK_NAME_INVALID = ("<b>Tautan tidak valid</b>. Tautan harus:\n"
                         "• mulailah dengan huruf\n"
                         "• terdiri secara eksklusif dari huruf, angka atau garis bawah\n"
                         "• tidak berisi dua garis bawah berturut-turut\n"
                         "• tidak diakhiri dengan garis bawah\n"
                         "\n"
                         "Silakan coba lagi")

    PACK_NAME_INVALID_MESSAGE = ("Oh tidak! Ini bukan yang saya tunggu! Tolong kirimkan saya "
                                 "tautan paket, atau /cancel")

    PACK_NAME_DUPLICATE = "Maaf, Anda sudah memiliki paket dengan tautan ini disimpan. coba dengan tautan lain"

    PACK_TYPE_BUTTONS_EXPIRED = "Tombol-tombol ini tidak lagi valid"

    PACK_TYPE_CHANGED = "Jenis paket: {}. Sekarang kirimkan saya judul paket!"

    PACK_CREATION_WAITING_FIRST_STATIC_STICKER = ("Mengerti, kita hampir selesai. Sekarang kirimkan saya stiker pertama "
                                                  "paket (atau file png, atau emoji yang digunakan untuk stiker)")

    PACK_CREATION_WAITING_FIRST_ANIMATED_STICKER = ("Mengerti, kita hampir selesai. Sekarang kirimkan saya animasi pertama "
                                                    "stiker paket (atau emoji yang digunakan untuk stiker)")

    PACK_CREATION_WAITING_FIRST_VIDEO_STICKER = ("Mengerti, kita hampir selesai. Sekarang kirimkan saya video pertama "
                                                    "stiker paket (atau emoji yang digunakan untuk stiker)")

    PACK_CREATION_FIRST_STICKER_PACK_DATA_MISSING = ("Ooops, ada yang tidak beres.\n"
                                                     "Silakan ulangi proses pembuatan dengan /create")

    PACK_CREATION_WAITING_FIRST_STICKER_INVALID_MESSAGE = ("Umm 🤔 saya sedang menunggu stiker pertama dari paket. "
                                                           "Tolong kirimkan saya stiker, atau /cancel")

    PACK_CREATION_ERROR_DUPLICATE_NAME = ("Maaf, sudah ada paket dengan <a href=\"{}\">tautan ini</a>.\n"
                                          "Please send me a new link, or /cancel")

    PACK_CREATION_ERROR_INVALID_NAME = ("Maaf, Telegram menolak tautan yang Anda berikan dengan mengatakan itu tidak valid.\n"
                                        "Silakan kirim tautan baru kepada saya, atau /cancel")

    PACK_CREATION_ERROR_GENERIC = ("Kesalahan saat mencoba membuat paket: <code>{}</code>.\n"
                                   "Silakan coba lagi, atau /cancel")

    PACK_CREATION_PACK_CREATED = ("Paket Anda telah dibuat, tambahkan melalui <a href=\"{}\">tautan ini</a>\n"
                                  "Terus kirimi saya stiker untuk menambahkan lebih banyak, atau /done")

    ADD_STICKER_SELECT_PACK = "Pilih paket yang ingin Anda tambahkan stiker, atau /cancel"

    ADD_STICKER_NO_PACKS = "Anda belum memiliki paket apa pun. Pakai /create untuk mulai membuat paket baru"

    ADD_STICKER_SELECTED_TITLE_DOESNT_EXIST = ("Sepertinya paketnya \"{}\" tidak ada.\n"
                                               "Silakan pilih paket yang valid dari keyboard")

    ADD_STICKER_SELECTED_TITLE_MULTIPLE = ("Sepertinya Anda memiliki banyak paket yang cocok dengan judulnya \"{}\".\n"
                                           "Silakan pilih paket yang ingin Anda pilih dari keyboard di bawah ini. Referensi paket:\n"
                                           "• {}")

    ADD_STICKER_PACK_SELECTED_STATIC = ("Bagus, kita akan menambahkan stiker ke <a href=\"{}\">Paket ini</a>.\n"
                                        "Kirimi saya stiker atau file png, atau /cancel")

    ADD_STICKER_PACK_SELECTED_ANIMATED = ("Bagus, kita akan menambahkan stiker ke <a href=\"{}\">Paket ini</a>.\n"
                                          "Kirimi saya stiker animasi, atau /cancel")

    ADD_STICKER_PACK_SELECTED_VIDEO = ("Bagus, kita akan menambahkan stiker ke <a href=\"{}\">Paket ini</a>.\n"
                                          "Kirimi saya stiker video atau file webp, atau /cancel")

    ADD_STICKER_SELECTED_NAME_DOESNT_EXIST = ("Sepertinya paketnya \"{}\" tidak ada.\n"
                                              "Silakan pilih paket yang valid dari keyboard")

    ADD_STICKER_PACK_DATA_MISSING = ("Ooops, ada yang tidak beres.\n"
                                     "Please repeat the process with /add")

    ADD_STICKER_PACK_NOT_VALID = ("Ooops, it looks like <a href=\"{}\">this pack</a> doesn't exist.\n"
                                  "Please select another pack")

    ADD_STICKER_PACK_NOT_VALID_NO_PACKS = ("Ooops, it looks like <a href=\"{}\">this pack</a> doesn't exist.\n"
                                           "Please create a new pack with /create")

    ADD_STICKER_NO_EMOJI_IN_TEXT = ("Uhm, I don't understand. Send me a stickers, or send me a list of emojis to "
                                    "use for the next stickers (or /done to exit)")

    ADD_STICKER_TOO_MANY_EMOJIS = "Whoa, that's a lot of emojis! I can only use 10 at max, please try again"

    ADD_STICKER_EMOJIS_SAVED = "Oh, some emojis! We will use these {} emojis for the next stickers you will send me: {}"

    ADD_STICKER_SUCCESS = ("Sticker added to <a href=\"{}\">this pack</a>. "
                           "Continue to send me stickers to add more, use /done when you're done")

    ADD_STICKER_SUCCESS_EMOJIS = ("Sticker added to <a href=\"{}\">this pack</a> using these emojis: {}\n"
                                  "Continue to send me stickers to add more, use /done when you're done")

    ADD_STICKER_PACK_FULL = ("I'm sorry, <a href=\"{}\">this pack</a> is full ({} stickers), "
                             "you can no longer add stickers to it. Use /remove to remove some stickers\n"
                             "You've exited the \"adding stickers\" mode")

    ADD_STICKER_SIZE_ERROR = ("Whoops, it looks like an error happened while resizing the stickers. "
                              "I can't add this stickers to the pack due to wrong resizing logic.\n"
                              "Send me another stickers, or use /done when you're done")

    ADD_STICKER_INVALID_ANIMATED = ("It looks like this stickers is no loger compliant with the most recent "
                                    "<a href=\"https://core.telegram.org/animated_stickers\">Telegram guidelines</a> "
                                    "about animated stickers. I'm sorry but I can't add it :(\n"
                                    "You can try to send the stickers again or "
                                    "send another animated stickers (or /cancel)")

    ADD_STICKER_FLOOD_EXCEPTION = ("Uh-oh, it looks like I'm quite busy right now. I cannot create the pack, or "
                                   "you've been creating too many packs lately. "
                                   "Please try again in: {} hours")

    ADD_STICKER_GENERIC_ERROR = ("An error occurred while adding this stickers to <a href=\"{}\">this pack</a>: "
                                 "<code>{}</code>.\n"
                                 "Try again, send me another stickers or use /done when you're done")

    ADD_STICKER_ANIMATED_UNSUPPORTED = ("I am sorry, I do not support animated stickers yet :(\n"
                                        "Please send a static stickers")

    ADD_STICKER_EXPECTING_DIFFERENT_TYPE = ("Uh-oh. I was waiting for a {} stickers, not a {} one. "
                                            "Please send me a new stickers, or /cancel")

    ADD_STICKER_INVALID_MESSAGE = "Uhmm 🤔 I was waiting for the stickers to add. Send me a stickers, or /cancel"

    REMOVE_STICKER_SELECT_STICKER = "Send me the stickers you want to remove from its pack, or /cancel"

    REMOVE_INVALID_MESSAGE = "Please send the stickers you want to remove from its pack, or /cancel"

    REMOVE_STICKER_SUCCESS = ("Sticker removed from <a href=\"{}\">its pack</a>.\n"
                              "Send me another stickers to remove, or /done when you're done")

    REMOVE_STICKER_FOREIGN_PACK = ("This stickers is from a <a href=\"{}\">pack</a> you didn't create through me. "
                                   "Try with a valid stickers, or /done")

    REMOVE_STICKER_ALREADY_DELETED = ("This stickers is no longer part of <a href=\"{}\">the pack</a>, "
                                      "try with another stickers, or /done")

    REMOVE_STICKER_GENERIC_ERROR = (
        "An error occurred while removing this stickers from <a href=\"{}\">this pack</a>: "
        "<code>{}</code>.\n"
        "Try again, send me another stickers or use /done when you're done")

    READD_WAITING_STICKER = "Please send me a stickers from the pack you " \
                                         "want to save among the packs I manage.\n" \
                                         "Please remember that the pack must have been created by me. " \
                                         "Use /cancel to cancel"

    READD_STICKER_NO_PACK = "This stickers does not belong to a pack. Please try with another pack, or /cancel"

    READD_STICKER_ANIMATED = "This only works with static (non-animated) stickers packs. Please try with another pack, or /cancel"

    READD_UNEXPECTED_MESSAGE = "Uuh, I don't understand what you're trying to say.\n" \
                               "Please send me the pack name/link of the pack to add (or send me a stickers from the pack), or /cancel"

    READD_WRONG_PACK_NAME = "I'm sorry, it looks like <a href=\"{}\">this pack</a>'s name doesn't end by \"<code>{}</code>\", " \
                            "therefore I don't own it: you can only add the packs I created. Try with another pack, or /cancel"

    READD_INVALID_PACK_NAME_PATTERN = "I'm sorry, it looks like this name is not a valid pack name. " \
                                      "A stickers's pack name is what comes after its share link " \
                                      "(<code>https://t.me/addstickers/</code> link).\n\n" \
                                      "Try again with another name/link, or send me a stickers from the pack, " \
                                      "or /cancel"

    READD_PACK_EXISTS = "It looks like <a href=\"{}\">this pack</a> is already saved in your packs. " \
                            "Try with another pack, or /cancel"

    READD_PACK_INVALID = "I'm sorry, it looks like you didn't create <a href=\"{}\">this pack</a> with me " \
                                  "(or it doesn't exists). " \
                                  "You can only add packs that were created by me.\n\n" \
                                  "Try with another pack, or /cancel"

    READD_UNKNOWN_API_EXCEPTION = "I'm sorry, it looks like you didn't create <a href=\"{}\">this pack</a> with me, " \
                                  "or it doesn't exists (error: <code>{}</code>). " \
                                  "You can only add packs that were created by me.\n\n" \
                                  "Try with another pack, or /cancel"

    READD_SAVED = "{} successfully saved to your packs!"

    READD_DUMMY_STICKER_NOT_REMOVED = "Anyway, to check whether I owned this pack or not, " \
                                      "I had to add a dummy stickers to the pack, which I haven't been able to remove. " \
                                      "You can remove it manually using the /remove command"

    READD_DUMMY_STICKER_NOT_REMOVED_UNKNOWN = "Anyway, to check whether I owned this pack or not, " \
                                              "I had to add a dummy stickers to the pack, " \
                                              "which I haven't been able to remove (<code>{}</code>). " \
                                              "You can remove it manually using the /remove command"

    FORGETME_SUCCESS = "Success, I've deleted all of your packs from my database"

    CANCEL = "Good, we're done with that"

    CANCEL_NO_CONVERSATION = "There is no operation going on 😴"

    TIMEOUT = "😴 It looks like you are inactive, I've canceled the current operation"

    LIST_NO_PACKS = "You don't have any pack. Use /create to create one"

    LIST_FOOTER = "\n\n<b>s</b>: static\n<b>a</b>: animated\n<b>v</b>: video"

    ANIMATED_STICKERS_NO_FILE = "Unfortunately I can't send you animated stickers back as file :("

    EXPORT_PACK_SELECT = "Please send me a sticker from the pack you want to export, or /cancel"

    EXPORT_PACK_NO_PACK = "This stickers doesn't belong to any pack. Please send me a stciker from a pack, or /cancel"

    EXPORT_PACK_START = "Exporting stickers from <i>{}</i>... it may take some minutes. Please hold on"

    EXPORT_PACK_UPLOADING = "Zipping png files and uploading..."

    EXPORT_ANIMATED_STICKERS_NOT_SUPPORTED = "Exporting animated packs is not supported yet"

    EXPORT_SKIPPED_STICKERS = " - I wasn't able to export {} stickers!"

    EXPORT_ONGOING = "Hold on, the export is processing..."

    CLEANUP_NO_PACK = ("It looks like all your packs are still there. No pack has been removed from the database.\n"
                       "If you just deleted a pack from @stickers, remember that it might take some time for bots "
                       "to be made aware of its deletion.\n\n"
                       "You can use /list to see the list of your packs")

    CLEANUP_HEADER = "These are the packs that no longer exist and has been removed from the database:\n"

    CLEANUP_WAIT = "Hold on, this operation might take some time..."

    TO_FILE_MIME_TYPE = "mime-type: {}"

    TO_EMOJI_WAITING_STICKER = "Send me a static sticker, " \
                               "I will send you back a file you can use as custom emoji"

    TO_EMOJI_UNEXPECTED_MESSAGE = "Please send me a <b>static</b> stickers, or /cancel"

    TO_EMOJI_NON_STATIC_STICKER = "Animated and video stickers don't need to be resized, you can use " \
                                  "<code>/tofile</code> to convert an animated/static sticker to a " \
                                  "cutom emoji-ready file. Use /done when you're done with this command"

    EMOJI_TO_FILE_VIDEO_NOT_SUPPORTED = "Video stickers are not supported 😔"

    EMOJI_TO_FILE_TOO_MANY_ENTITIES = "Please send just one custom emoji"

    TO_FILE_WAITING_STICKER = "Please send the stickers (static/video) or the custom emoji you want to convert to " \
                              "file, or /cancel"

    TO_FILE_UNEXPECTED_MESSAGE = "I wasn't expecting that 🤔 please send a stickers or a custom emoji, or use /cancel"

    ENABLED_FLAGS = "Enabled flags: "
