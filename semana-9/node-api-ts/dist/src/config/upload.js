"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const multer_1 = __importDefault(require("multer"));
const multer_s3_1 = __importDefault(require("multer-s3"));
const s3_1 = __importDefault(require("./s3"));
const upload = (0, multer_1.default)({
    storage: (0, multer_s3_1.default)({
        s3: s3_1.default,
        bucket: process.env.AWS_S3_BUCKET_NAME,
        metadata: (_req, file, cb) => {
            cb(null, {
                fieldName: file.fieldname,
            });
        },
        key: (_req, file, cb) => {
            cb(null, `${Date.now()}-${file.originalname}`);
        },
    }),
});
exports.default = upload;
